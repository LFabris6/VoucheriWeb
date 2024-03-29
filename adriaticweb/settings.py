import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import firebase_admin
from firebase_admin import credentials

cred_path = os.path.join(BASE_DIR, "static", "apikey.json")

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q^r5rkqho5ck+271z7yla=5)3au876(h0m-dwjcvovj$d9_(_z'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
ALLOWED_HOSTS = ['mpstafftest.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "web",
    "pwa",
    'fcm_django',
    'rest_framework',
    'rest_framework.authtoken',
]

FCM_DJANGO_SETTINGS = {

    "APP_VERBOSE_NAME": "My App",

    "ONE_DEVICE_PER_USER" : False,

    "DELETE_INACTIVE_DEVICES": True,
}

PWA_APP_NAME = 'My App'
PWA_APP_DESCRIPTION = "My app description" 
PWA_APP_THEME_COLOR = '#0A0302' 
PWA_APP_BACKGROUND_COLOR = '#ffffff' 
PWA_APP_DISPLAY = 'standalone' 
PWA_APP_SCOPE = '/' 
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default' 
PWA_APP_ICONS = [ { 'src': '/static/img/mplogo.png', 'sizes': '180x180' } ] 
PWA_APP_ICONS_APPLE = [ { 'src': '/static/img/mplogo.png', 'sizes': '180x180' } ] 
PWA_APP_SPLASH_SCREEN = [ { 'src': '/static/img/mplogo.png', 'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)' } ] 
PWA_APP_DIR = 'ltr' 
PWA_APP_LANG = 'en-US'

PWA_APP_DEBUG_MODE = False


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'adriaticweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'adriaticweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators




# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = [
    #os.path.join(BASE_DIR, 'static')
#]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'adriaticwebdev@gmail.com'
EMAIL_HOST_PASSWORD = 'TVwn2D3j'
