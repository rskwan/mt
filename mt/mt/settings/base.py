import os
from unipath import Path

from django.core.exceptions import ImproperlyConfigured

import dj_database_url

def env_var(var_name):
    """Get the environment variable var_name or return an exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        msg = "Please set the environment variable {}".format(var_name)
        raise ImproperlyConfigured(msg)

SECRET_KEY = env_var("MT_SECRET_KEY")

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# ADMIN_PATH controls where the admin urls are.
# e.g. if ADMIN_PATH == 'adminsitemilktea', then the admin site
# should be available at /adminsitemilktea/ instead of /admin/.
ADMIN_PATH = env_var("MT_ADMIN_PATH")

DJANGO_CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'djmoney',
    'nested_admin',
]

CUSTOM_APPS = [
    'core',
]

INSTALLED_APPS = DJANGO_CORE_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mt.urls'
WSGI_APPLICATION = 'mt.wsgi.application'

BASE_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = BASE_DIR.child("media")
STATIC_ROOT = BASE_DIR.child("static")
STATICFILES_DIRS = (
    BASE_DIR.child("assets"),
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (BASE_DIR.child("templates"),),
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

DATABASES = {'default': dj_database_url.parse(env_var("MT_MYSQL_URL"), conn_max_age = 600)}
DATABASES['default']['ATOMIC_REQUESTS'] = True

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


TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
