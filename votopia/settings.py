from pathlib import Path
from decouple import config, Csv
import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Load secret key from .env
SECRET_KEY = config('SECRET_KEY')

# Load Debug from .env
DEBUG = config('DEBUG', default=False, cast=bool)

# Load Allowed Hosts from .env
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'manager',
    'voting',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'votopia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['voting/template', 'manager/template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'votopia.wsgi.application'

# Database Configuration using .env
DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': BASE_DIR / config('DB_NAME'),
    }
}

DATABASES["default"] = dj_database_url.parse(
    config('DATABASE_URL')
)


DATABASES["default"] = dj_database_url.parse("postgresql://votopia_db_user:LveatabVWk0Fxz4BhfTqZfb76aqGULf2@dpg-crnlbso8fa8c738i3r10-a.oregon-postgres.render.com/votopia_db")
# Other settings...

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

AUTH_USER_MODEL = 'account.CustomUser'
AUTHENTICATION_BACKEND = ['account.email_backend.EmailBackend']

# Load Election Title Path from .env
ELECTION_TITLE_PATH = os.path.join(BASE_DIR, config('ELECTION_TITLE_PATH'))

SEND_OTP = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
