"""
Django settings for horseracing project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f0ujzwp%^pc+%av_s+1%g=533_o@8&_1&vxykycarqrz$m7_!-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['genesis-data.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'frontend',
    'django_q'
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

ROOT_URLCONF = 'horseracing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'horseracing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'horseracing',
        'USER': 'postgres',
        'PASSWORD':'postgres',
        'HOST': 'localhost'
    }
}
if DEBUG is False:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

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
#Authentication backends
AUTHENTICATION_BACKENDS = [ 'django.contrib.auth.backends.ModelBackend' ]

AUTH_USER_MODEL = 'frontend.User'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
if DEBUG is False:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if DEBUG :
    Q_CLUSTER = {
        'name': 'horseracing',
        'label': 'Django Q',
        "workers": 1,
        "timeout": 3600,
        "retry": 4600,
        "queue_limit": 50,
        "bulk": 10,
        'redis': {
            'host': '127.0.0.1',
            'port': 6379,
            'db': 0, 
        }
    }
else:
    Q_CLUSTER = {
        'name': 'horseracing',
        'label': 'Django Q',
        "workers": 8,
        "timeout": 60*60*9,
        "retry": 60*60*10,
        'save_limit': 250,
        "queue_limit": 500,
        "bulk": 10,
        'redis': {
            'host': 'ec2-54-90-41-195.compute-1.amazonaws.com',
            'port': 10400,
            'password': 'pf01379312ff47131e6784005ae4c1b3f88e766ff576fa2701f4f5b6a65a69ae5',
            'db': 0, 
            'health_check_interval': 10,
            'socket_timeout': 10,
            'socket_keepalive': True,
            'socket_connect_timeout': 10, 
            'retry_on_timeout': True,
            'ssl': True,
            'ssl_cert_reqs': None
        }
        # 'redis': 'rediss://:pf01379312ff47131e6784005ae4c1b3f88e766ff576fa2701f4f5b6a65a69ae5@ec2-54-90-41-195.compute-1.amazonaws.com:10400'
    }
