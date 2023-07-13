import os
from . base import *

DEBUG = False

ADMINS = [
    ('admin', 'admin@localhost'),
]

ALLOWED_HOSTS = ['educasite.com', 'www.educasite.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

# Безопасность
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


# openssl req -x509 -newkey rsa:2048 -sha256 -days 3650 -nodes \
#  keyout ssl/educa.key -out ssl/educa.crt \
#  subj '/CN=*.educasite.com' \
#  addext 'subjectAltName=DNS:*.educasite.com'