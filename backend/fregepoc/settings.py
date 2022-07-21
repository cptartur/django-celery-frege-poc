"""
Django settings for fregepoc project.
Generated by 'django-admin startproject' using Django 4.0.3.
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-18a(26fjpz)=w8kab)^gja983f#bn*g^zp#_33sv0hxb#o0aoe"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "true").lower() == "true"

ALLOWED_HOSTS = [os.environ.get("BACKEND_HOSTNAME", ".localhost")]

DJANGO_CORS_ALLOWED_HOSTS = [
    os.environ.get("FRONTEND_URL", "http://localhost:4200")
]

# Application definition

PROJECT_APPS = [
    "fregepoc",
    "fregepoc.repositories.apps.RepositoriesConfig",
    "fregepoc.indexers.apps.IndexersConfig",
    "fregepoc.analyzers.apps.AnalyzersConfig",
]

EXTERNAL_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "rest_framework",
    "rest_framework_api_key",
    "corsheaders",
    "django_filters",
    "channels",
]

INSTALLED_APPS = EXTERNAL_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "fregepoc.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "fregepoc.wsgi.application"
ASGI_APPLICATION = "fregepoc.asgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "api_static/"
STATIC_ROOT = BASE_DIR / "static"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# DATABASES
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DJANGO_DATABASE_NAME", "frege"),
        "USER": os.environ.get("DJANGO_DATABASE_USER", "frege"),
        "PASSWORD": os.environ.get("DJANGO_DATABASE_PASSWORD", "admin"),
        "HOST": os.environ.get("DJANGO_DATABASE_HOST", "127.0.0.1"),
        "PORT": os.environ.get("DOCKER_POSTGRES_PORT", "15432"),
    }
}

REDIS_HOST = os.environ.get("DJANGO_REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.environ.get("DJANGO_REDIS_PORT", "16379")

# CELERY STUFF
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
# CELERY_IMPORTS = ("fregepoc.repositories.celery_tasks",)

CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/"
CELERY_CACHE_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/"

# CACHE

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/",
    }
}

# MISC

DOWNLOAD_PATH = os.environ.get("DJANGO_DOWNLOAD_PATH", "/var/tmp/frege/")

# REST FRAMEWORK

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "fregepoc.utils.throttling.ApiKeyRateThrottle"
    ],
    "DEFAULT_THROTTLE_RATES": {"apikey": "500/minute"},
}

# CORS

CORS_ALLOWED_ORIGINS = [
    # set for production
]

# CHANNELS

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(REDIS_HOST, REDIS_PORT)],
        },
    },
}
