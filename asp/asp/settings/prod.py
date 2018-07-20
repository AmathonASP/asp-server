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
