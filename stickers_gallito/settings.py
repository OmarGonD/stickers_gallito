import os
from decouple import config

# SITE_ROOT = root()


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'stickers-gallito-app.herokuapp.com',
                 'stickersgallito.pe', 'www.stickersgallito.pe']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'search_app',
    'cart',
    'stripe',
    'order',
    'crispy_forms',
    'embed_video',
    'storages',
    'marketing',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'stickers_gallito.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'shop', 'templates/'),
                 os.path.join(BASE_DIR, 'search_app', 'templates/'),
                 os.path.join(BASE_DIR, 'cart', 'templates/'),
                 os.path.join(BASE_DIR, 'order', 'templates/'), ]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processor.menu_links',
                'shop.context_processor.has_shop',
                # 'cart.context_processor.current_time',
                'cart.context_processor.cart_items_counter'
            ],
        },
    },
]

WSGI_APPLICATION = 'stickers_gallito.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


# SECURITY WARNING: don't run with debug turned on in production!


if DEBUG:
    # Redirecciona www y http  a https
    SECURE_SSL_REDIRECT = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

else:

    # Redirecciona www y http  a https
    SECURE_SSL_REDIRECT = True

    ### HEROKU POSTGRESS ACCESS
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('HEROKU_POSTGRESQL_NAME'),
            'USER': config('HEROKU_POSTGRESQL_USER'),
            'PASSWORD': config('HEROKU_POSTGRESQL_PASSWORD'),
            'HOST': config('HEROKU_POSTGRESQL_HOST'),
            'PORT': config('HEROKU_POSTGRESQL_PORT'),
        }
    }

####

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

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

####


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

### CULQUI ###


CULQI_PUBLISHABLE_KEY = os.environ['CULQI_PUBLISHABLE_KEY']

CULQI_SECRET_KEY = os.environ['CULQI_SECRET_KEY']

# DO NOT DO THIS!
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']
MAILCHIMP_DATA_CENTER = os.environ['MAILCHIMP_DATA_CENTER']
MAILCHIMP_EMAIL_LIST_ID = os.environ['MAILCHIMP_EMAIL_LIST_ID']

### AMAZON ###


AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']
# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

### MAILGUN - EMAIL MESSAGE SETTINGS ###

EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
