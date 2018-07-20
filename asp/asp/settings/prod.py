from .common import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aspDB',
#        'NAME': 'danoshop_crawl',
        'USER': 'asp',
        'PASSWORD': 'amathonasp1!',
#        'HOST': '10.33.1.216',
        'HOST': 'amathon-asp.c31ynxumvgwl.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB, character_set_connection=utf8mb4, collation_connection=utf8mb4_unicode_ci',
            'charset':'utf8mb4',
        },
    },
}

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# # AWS Setting
# AWS_REGION = 'ap-northeast-2c'
# AWS_STORAGE_BUCKET_NAME = 'asp-audio-storage'
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
# AWS_ACCESS_KEY_ID = 'AKIAJR4VHTZROWTFGAUA'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# # #Media Setting
# # MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# # MEDIA_ROOT = MEDIA_URL
