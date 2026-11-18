from django import forms
from django.conf import settings
from .models import Contact, HireRequest, SupportSettings


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 transition-all',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 transition-all',
                'placeholder': 'your.email@example.com'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 transition-all',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 transition-all min-h-[150px]',
                'placeholder': 'Your message...',
                'rows': 5
            }),
        }


class SupportForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'id': 'id_support_name',
            'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 transition-all',
            'placeholder': 'Your name (optional)',
            'autocomplete': 'name',
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'id_support_email',
            'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 transition-all',
            'placeholder': 'you@example.com',
            'autocomplete': 'email',
        }),
    )
    amount = forms.IntegerField(
        min_value=100,
        max_value=5_000_000,
        widget=forms.NumberInput(attrs={
            'id': 'support-amount',
            'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 transition-all',
            'min': '100',
            'max': '5000000',
            'step': '100',
            'inputmode': 'numeric',
        }),
    )


class HireRequestForm(forms.ModelForm):
    project_type = forms.ChoiceField(
        choices=HireRequest.PROJECT_TYPE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500'}),
    )
    budget = forms.ChoiceField(
        choices=HireRequest.BUDGET_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500'}),
    )
    timeline = forms.ChoiceField(
        choices=HireRequest.TIMELINE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500'}),
    )

    class Meta:
        model = HireRequest
        fields = ['name', 'email', 'company', 'project_type', 'budget', 'timeline', 'project_details']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500', 'autocomplete': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500', 'autocomplete': 'email'}),
            'company': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500', 'autocomplete': 'organization'}),
            'project_details': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-lg bg-slate-800 border border-slate-700 text-slate-100 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 min-h-[150px]', 'rows': 6}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Your name'
        self.fields['email'].label = 'Email address'
        self.fields['company'].required = False
        self.fields['company'].label = 'Company (optional)'
        self.fields['project_details'].label = 'Tell me about the project'


class SupportSettingsForm(forms.ModelForm):
    paystack_secret_key = forms.CharField(
        required=False,
        label='Paystack Secret Key',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='Enter a test or live secret key. It is encrypted before it is stored and never shown again.',
    )
    clear_paystack_secret = forms.BooleanField(
        required=False,
        label='Remove the saved Paystack secret key',
    )

    class Meta:
        model = SupportSettings
        fields = ['title', 'suggested_amounts', 'is_active']

    def clean(self):
        cleaned_data = super().clean()
        secret = cleaned_data.get('paystack_secret_key')
        clear_secret = cleaned_data.get('clear_paystack_secret')
        if (secret or clear_secret) and not settings.PAYSTACK_CREDENTIALS_ENCRYPTION_KEY:
            self.add_error(
                'paystack_secret_key',
                'Set DJANGO_SECRET_KEY in the server environment before managing Paystack credentials.',
            )
        if secret and clear_secret:
            self.add_error(
                'clear_paystack_secret',
                'Choose either a new secret key or remove the saved key, not both.',
            )
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get('clear_paystack_secret'):
            instance.set_paystack_secret('')
        elif self.cleaned_data.get('paystack_secret_key'):
            instance.set_paystack_secret(self.cleaned_data['paystack_secret_key'])
        if commit:
            instance.save()
            self.save_m2m()
        return instance
