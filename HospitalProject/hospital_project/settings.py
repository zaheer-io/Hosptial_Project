"""
Django settings for hospital_project project.
Care Point Hospital Management System
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# We override this in environment variables for Render & PythonAnywhere
SECRET_KEY = os.environ.get("SECRET_KEY", "your-local-dev-secret-key")

# DEBUG should be False in production
DEBUG = os.environ.get("DEBUG", "False") == "True"

# Dynamic ALLOWED_HOSTS works for PythonAnywhere, Render, and local dev
ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS", "ourcarepoint.pythonanywhere.com"
).split(",")


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Hospital Apps
    'accounts',
    'departments',
    'doctors',
    'patients',
    'appointments',
    'pharmacy',
    'billing',
    'adminpanel',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # For Render static hosting
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hospital_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hospital_project.wsgi.application'


# Database
# IMPORTANT:
# - PythonAnywhere uses SQLite3 by default unless you add MySQL/Postgres
# - Render uses Postgres with a DATABASE_URL env var
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',    # For local & PythonAnywhere free tier
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# If Render DATABASE_URL exists, override the default DB config
DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    import dj_database_url
    DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Same STATIC_ROOT works for both Render + PythonAnywhere
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Whitenoise static compression
WHITENOISE_KEEP_ONLY_HASHED_FILES = True


# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Custom User model
AUTH_USER_MODEL = 'accounts.User'


# Login redirects
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'accounts:redirect_after_login'
LOGOUT_REDIRECT_URL = 'accounts:login'


# Razorpay Keys (test mode)
RAZORPAY_KEY_ID = os.environ.get("RAZORPAY_KEY_ID", "rzp_test_Rn84o8Z3bbux28")
RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET", "yVgDzj7J3Nn6xlPl3tzkNrRX")


# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
