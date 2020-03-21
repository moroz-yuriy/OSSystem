# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Grabs the site root setup in settings.py
import os
import OSSystem.settings as settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}
