

import os

from boto.s3.connection import S3Connection


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^_67&#r+(c+%pu&n+a%&dmxql^i^_$0f69)mnhf@)zq-rbxe9z'



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
    'marketing'

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
                 os.path.join(BASE_DIR, 'order', 'templates/'),]
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


### HEROKU POSTGRESS ACCESS

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddvdrmi0vj51t1',
        'USER': 'u411dcl7sjn1gv',
        'PASSWORD': 'p7b6265f772f4c45a5c881a1d7b7fef659703707cadb6fd2d8696f642015fbac1',
        'HOST': 'ec2-34-226-163-183.compute-1.amazonaws.com',
        'PORT': '5432',
        # 'OPTIONS': {
        #     'sslmodule': 'required'
        # }
    }
}


####

# add this
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# you run `collectstatic`).


STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'



MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'


### Amazon S3

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}


AWS_STORAGE_BUCKET_NAME = 'stickers-gallito-uploaded-files'
AWS_S3_REGION_NAME = 'us-east-2'  # e.g. us-east-2
# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

####


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')



CRISPY_TEMPLATE_PACK = 'bootstrap4'


### CULQUI ###


# CULQI_PUBLISHABLE_KEY = S3Connection(os.environ['CULQI_PUBLISHABLE_KEY'])
#
# CULQI_SECRET_KEY = S3Connection(os.environ['CULQI_SECRET_KEY'])

CULQI_PUBLISHABLE_KEY = "test"

CULQI_SECRET_KEY = "test"



# DO NOT DO THIS!
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


#Redirecciona www y http  a https
SECURE_SSL_REDIRECT = False

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



MAILCHIMP_API_KEY = "b87c5a8b98831568e12087f9a8a8b49b-us20"
MAILCHIMP_DATA_CENTER = 'us20'
MAILCHIMP_EMAIL_LIST_ID = '9137cdc305'

### AMAZON ###


# AWS_ACCESS_KEY_ID = S3Connection(os.environ['AWS_ACCESS_KEY_ID'])
#
# AWS_SECRET_ACCESS_KEY = S3Connection(os.environ['AWS_SECRET_ACCESS_KEY'])

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']



# AWS_ACCESS_KEY_ID = 'AKIAIOMYOFWZLUBDB3OA'
# AWS_SECRET_ACCESS_KEY = '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'
#


### EMAIL MESSAGE SETTINGS ###

# EMAIL_HOST = S3Connection(os.environ['EMAIL_HOST'])
# EMAIL_PORT = S3Connection(os.environ['EMAIL_PORT'])
# EMAIL_USE_TLS = S3Connection(os.environ['EMAIL_USE_TLS'])
# EMAIL_HOST_USER = S3Connection(os.environ['EMAIL_HOST_USER'])
# EMAIL_HOST_PASSWORD = S3Connection(os.environ['EMAIL_HOST_PASSWORD'])


EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'postmaster@email.stickersgallito.pe'
EMAIL_HOST_PASSWORD = "0e72c0deb828b9f57112933a40c5d649-de7062c6-c8a2023e"