from .base import *

DEBUG = True

THIRD_PARTY_APPS += ['debug_toolbar']
INSTALLED_APPS = DJANGO_CORE_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
