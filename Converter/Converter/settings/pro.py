from .base import *
DEBUG = False
ADMINS = (
    ('Nick S', 'nstenquist@sandy.utah.gov')
)
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3")),
    }
}