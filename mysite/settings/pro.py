from .base import *

DEBUG = False

ADMINS = (
    ('admin', 'admin@admin.com'),
)

ALLOWED_HOSTS = ['mysiteproject.com', 'www.mysiteproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydatabase',
        'USER': 'nli',
        'PASSWORD': 'secret',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
