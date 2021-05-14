# import os
# import sys
# from unipath import Path
# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# from celery import app
from __future__ import absolute_import
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

import os,sys
import datetime
from unipath import Path

from celery.schedules import crontab
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = Path(__file__).ancestor(2)
PROJECT_APPS = Path(__file__).ancestor(2)
sys.path.insert(0, Path(PROJECT_APPS, 'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l*e=_yny4&^9hs#qlmlg78!fh*7409s8t#7$@8y#8p3-x==k+f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'apps.dashboard',
    'apps.authentication',
    'apps.pay',
    'celery',
    'import_export',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
]


SITE_ID = 1
X_FRAME_OPTIONS='SAMEORIGIN'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

CACHE_MIDDLEWARE_SECONDS= 5
CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
      'LOCATION': 'techbox_cache',
   }
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
               'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':(
                'rest_framework.permissions.IsAuthenticated',
    ),

}

ROOT_URLCONF = 'techbox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'techbox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'hi'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR,"media")
MEDIA_URL = '/media/'
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/'
# config/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "mdeeppatidar@gmail.com"
EMAIL_HOST_PASSWORD = "Deepak@9399@"

# CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
CELERY_IMPORTS = ['dashboard.task']
# from celery.schedules import crontab

# CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_TIMEZONE = 'Asia/Kolkata'
# # Let's make things happen
# #  'send-summary-every-hour': {
# #        'task': 'summary',
# #         # There are 4 ways we can handle time, read further
# #        'schedule': 5.0,
# #         # If you're using any arguments
# #        'args': ("We don’t need any",),
# #     },
    # Executes every Friday at 4pm
# CELERY_BEAT_SCHEDULE = {
#     "send-notification-on-friday-afternoon": {
#          "task": "apps.dashboard.task.send_notification",
#         #  'schedule': crontab(hour=16, day_of_week=5),
#             "schedule": 5.0,

#         },
# }
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# sentry
sentry_sdk.init(
    dsn="https://fe5a87c0befe4bcf89a49b5c3d97c159@o578639.ingest.sentry.io/5734982",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

STRIPE_PUBLISHABLE_KEY = 'pk_test_51ImfcKSC4t3SvztxWsB7OwQDw269DCG0uUYVr9843yH4OvsWBuENqMOWzIVT2mJKmfHMsRLvcjTz85huT3QhlvFH00DSV8eDd3'
STRIPE_SECRET_KEY = 'sk_test_51ImfcKSC4t3SvztxvzEY37TgMIkxD34qRwflOgBHZ7v3AAPnKcDrXP8OnTfckmp0hiICwl16ZoCnzRsqq3j9JJ0x00gqQ3jj2y'
