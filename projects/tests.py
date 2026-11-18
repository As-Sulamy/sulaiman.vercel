from unittest.mock import Mock, patch

from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase, override_settings
from django.urls import reverse

from .forms import SupportForm, SupportSettingsForm
from .models import HireRequest, Inspiration, SupportSettings


class SupportFormTests(SimpleTestCase):
    def test_amount_must_be_within_supported_range(self):
        for amount in (99, 5_000_001):
            with self.subTest(amount=amount):
                form = SupportForm({'email': 'supporter@example.com', 'amount': amount})
                self.assertFalse(form.is_valid())


class SupportFlowTests(TestCase):
    @override_settings(PAYSTACK_SECRET_KEY='')
    @patch('projects.views.requests.post')
    def test_checkout_is_not_started_without_a_secret_key(self, post):
        response = self.client.post(
            reverse('support_start'),
            {'name': '', 'email': 'supporter@example.com', 'amount': '2000'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Online support payments are not available right now.')
        post.assert_not_called()

    @override_settings(PAYSTACK_SECRET_KEY='sk_test_example')
    @patch('projects.views.requests.post')
    def test_start_redirects_to_paystack_with_amount_in_kobo(self, post):
        paystack_response = Mock()
        paystack_response.json.return_value = {
            'status': True,
            'data': {'authorization_url': 'https://checkout.paystack.com/example'},
        }
        post.return_value = paystack_response

        response = self.client.post(
            reverse('support_start'),
            {'name': 'Supporter', 'email': 'supporter@example.com', 'amount': '2000'},
        )

        self.assertRedirects(
            response,
            'https://checkout.paystack.com/example',
            fetch_redirect_response=False,
        )
        self.assertEqual(post.call_args.kwargs['json']['amount'], 200_000)
        self.assertEqual(post.call_args.kwargs['json']['currency'], 'NGN')
        self.assertEqual(
            post.call_args.kwargs['json']['callback_url'],
            'http://testserver/support/callback/',
        )

    @override_settings(
        PAYSTACK_SECRET_KEY='',
        PAYSTACK_CREDENTIALS_ENCRYPTION_KEY='test encryption key',
    )
    @patch('projects.views.requests.post')
    def test_start_uses_secret_saved_in_admin_settings(self, post):
        support_settings = SupportSettings()
        support_settings.set_paystack_secret('sk_test_admin_secret')
        support_settings.save()
        paystack_response = Mock()
        paystack_response.json.return_value = {
            'status': True,
            'data': {'authorization_url': 'https://checkout.paystack.com/example'},
        }
        post.return_value = paystack_response

        self.client.post(
            reverse('support_start'),
            {'name': 'Supporter', 'email': 'supporter@example.com', 'amount': '5000'},
        )

        self.assertEqual(
            post.call_args.kwargs['headers']['Authorization'],
            'Bearer sk_test_admin_secret',
        )

    @override_settings(PAYSTACK_SECRET_KEY='sk_test_example')
    @patch('projects.views.requests.get')
    def test_callback_verifies_payment_before_showing_success(self, get):
        paystack_response = Mock()
        paystack_response.json.return_value = {
            'status': True,
            'data': {'status': 'success', 'currency': 'NGN'},
        }
        get.return_value = paystack_response

        response = self.client.get(
            reverse('support_callback'),
            {'reference': 'support_ref_123'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Thank you for supporting my work!')
        self.assertEqual(
            get.call_args.args[0],
            'https://api.paystack.co/transaction/verify/support_ref_123',
        )

    @patch('projects.views.requests.get')
    def test_callback_rejects_invalid_reference_without_calling_paystack(self, get):
        response = self.client.get(
            reverse('support_callback'),
            {'reference': 'not/a/reference'},
        )

        self.assertEqual(response.status_code, 302)
        get.assert_not_called()


class InspirationPageTests(TestCase):
    def test_active_inspirations_are_rendered(self):
        Inspiration.objects.create(
            name='Ada Lovelace',
            role='Computer programming pioneer',
            is_active=True,
        )

        response = self.client.get(reverse('inspiration'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ada Lovelace')
        self.assertContains(response, 'data-tree-detail="my-profile-details"')
        self.assertContains(response, 'data-tree-detail="inspiration-details-')
        self.assertContains(response, 'style="--tree-node-delay: 1300ms"')

    def test_inactive_inspirations_are_not_rendered(self):
        Inspiration.objects.create(name='Hidden entry', is_active=False)

        response = self.client.get(reverse('inspiration'))

        self.assertNotContains(response, 'Hidden entry')


class SupportSettingsTests(TestCase):
    @override_settings(PAYSTACK_CREDENTIALS_ENCRYPTION_KEY='test encryption key')
    def test_paystack_secret_is_encrypted_before_storage(self):
        secret = 'sk_test_sensitive_value'
        support_settings = SupportSettings()

        support_settings.set_paystack_secret(secret)

        self.assertNotIn(secret, support_settings.paystack_secret_encrypted)
        self.assertEqual(support_settings.get_paystack_secret(), secret)

    @override_settings(PAYSTACK_CREDENTIALS_ENCRYPTION_KEY='test encryption key')
    def test_admin_settings_form_saves_secret_encrypted(self):
        form = SupportSettingsForm(data={
            'title': 'Support the work',
            'suggested_amounts': '[2000, 5000, 10000]',
            'is_active': 'on',
            'paystack_secret_key': 'sk_test_admin_value',
            'clear_paystack_secret': '',
        })

        self.assertTrue(form.is_valid(), form.errors)
        support_settings = form.save()

        self.assertNotIn('sk_test_admin_value', support_settings.paystack_secret_encrypted)
        self.assertEqual(support_settings.get_paystack_secret(), 'sk_test_admin_value')

    @override_settings(PAYSTACK_CREDENTIALS_ENCRYPTION_KEY='')
    def test_admin_does_not_accept_secret_without_encryption_key(self):
        form = SupportSettingsForm(data={
            'title': 'Support the work',
            'suggested_amounts': '[2000, 5000]',
            'is_active': 'on',
            'paystack_secret_key': 'sk_test_admin_value',
            'clear_paystack_secret': '',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('DJANGO_SECRET_KEY', str(form.errors))

    def test_paystack_secret_field_is_available_in_admin(self):
        user_model = get_user_model()
        user = user_model.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='test-password',
        )
        self.client.force_login(user)

        response = self.client.get(reverse('admin:projects_supportsettings_add'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Paystack Secret Key')
        self.assertContains(response, 'type="password"')


class HireMeTests(TestCase):
    def test_hire_me_form_is_separate_and_saves_project_inquiry(self):
        response = self.client.post(
            reverse('hire_me'),
            {
                'name': 'Client Name',
                'email': 'client@example.com',
                'company': 'Example Co',
                'project_type': 'website',
                'budget': '100k-500k',
                'timeline': '1-month',
                'project_details': 'I need a portfolio website.',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(HireRequest.objects.count(), 1)
        self.assertContains(response, 'Your project inquiry has been sent.')
        self.assertContains(response, 'Project inquiry')
        self.assertContains(self.client.get(reverse('contact')), 'Send a Message')

    def test_support_bar_and_modal_are_available_on_other_pages(self):
        response = self.client.get(reverse('contact'))

        self.assertContains(response, 'id="support-dialog"')
        self.assertContains(response, 'data-support-open-amount="2000"')
        self.assertContains(response, 'data-support-open-other')
