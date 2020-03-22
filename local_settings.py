# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Grabs the site root setup in settings.py
import os
import OSSystem.settings as settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}
