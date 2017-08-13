"""
Django settings for sysgate project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import dj_database_url
from decouple import config
from unipath import Path

SITE_NAME = 'SYSGate'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_DIR = Path(__file__).parent

LOGIN_URL = '/account/'
LOGIN_REDIRECT_URL = '/account/'

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

FIXTURE_DIRS = (
    PROJECT_DIR.child('fixtures'),
)

# Cargando desde un fichero externo lo convertimos en realmente secreto
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# En desarrollo lo permitimos todo
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'account',
    'apps.core',
    'apps.metrics',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

loaders = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader']

context_processors = [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR.child('templates')],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': context_processors,
            'loaders': loaders,
        },
    },
]

WSGI_APPLICATION = 'sysgate.wsgi.application'


# Nos permite expresar nuestro backend de forma mucho más programatica
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL')),
}


AUTH_USER_MODEL = 'account.User'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
