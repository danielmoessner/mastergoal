from .base import *

# Secret Settings

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", 'localhost']

# Application definition

# INSTALLED_APPS = ['django_gulp'] + INSTALLED_APPS

INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# Other

INTERNAL_IPS = ["127.0.0.1"]

# Cors to allow my fronted app to make requests

CORS_ALLOWED_ORIGINS += [
    "http://localhost:8080",
    'http://192.168.1.66:8080'
]
