"""
Django settings for portfolio project.
"""

from pathlib import Path
import os
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() == 'true' and not os.environ.get('VERCEL')
DJANGO_SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '').strip()
if not DEBUG and not DJANGO_SECRET_KEY:
    raise ImproperlyConfigured('Set DJANGO_SECRET_KEY in production.')
SECRET_KEY = DJANGO_SECRET_KEY or 'local-development-only-secret-key'
PAYSTACK_CREDENTIALS_ENCRYPTION_KEY = DJANGO_SECRET_KEY

ALLOWED_HOSTS = ['*', '.vercel.app', '127.0.0.1', '.now.sh']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'markdownx',
    'projects',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'projects.context_processors.portfolio_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django_mongodb_backend",
#         "HOST": "mongodb+srv://sulaimanbello249_db_user:VQ3vdb9Hz0zt2M3n@myportfolio.h0ekt6p.mongodb.net/",
#         "NAME": "sample_mflix",  # or the name of your database
#     },
# }

# sulaimanbello249_db_user
# VQ3vdb9Hz0zt2M3n

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': 'uQtOmDyLjSfcgdzoMruWizkrBGqTJnFP',
#         'HOST': 'mainline.proxy.rlwy.net',
#         'PORT': '15695',
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
PAYSTACK_SECRET_KEY = os.environ.get('PAYSTACK_SECRET_KEY', '').strip()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

# Email Configuration for Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your.email@gmail.com'  # Replace with your Gmail address
EMAIL_HOST_PASSWORD = 'your-app-password'  # Replace with your Gmail App Password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CONTACT_EMAIL = 'your.email@gmail.com'  # Email where you want to receive messages
