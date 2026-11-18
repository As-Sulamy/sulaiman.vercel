from django.conf import settings
from .forms import SupportForm
from .models import Education, Experience, Profile, Service, Skill, SocialLink, SupportSettings


def portfolio_context(request):
    support_settings = SupportSettings.objects.first() or SupportSettings()
    suggested_amounts = support_settings.suggested_amounts
    default_support_amount = suggested_amounts[1] if len(suggested_amounts) > 1 else suggested_amounts[0]
    return {
        'profile': Profile.objects.first(),
        'social_links': SocialLink.objects.filter(is_active=True),
        'skills': Skill.objects.filter(is_active=True),
        'experiences': Experience.objects.filter(is_active=True),
        'education': Education.objects.filter(is_active=True),
        'services': Service.objects.filter(is_active=True),
        'support_settings': support_settings,
        'support_form': SupportForm(initial={'amount': default_support_amount}),
        'support_default_amount': default_support_amount,
        'paystack_enabled': bool(
            support_settings.is_active
            and (
                settings.PAYSTACK_SECRET_KEY
                or support_settings.has_paystack_secret
            )
        ),
    }
