import os
from datetime import timedelta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = '008p$it5*b=-3nv!%lo6@s7^qs)&g!&vbsjwz1m9g_l6hhwdl+'
DEBUG = True
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "rest_framework_simplejwt",
    'rest_framework_simplejwt.token_blacklist',
    'django_extensions',
    'django_filters',
    'api',
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


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 7,
}

AUTH_USER_MODEL = "api.User"
AUTHENTICATION_BACKENDS = ["api.backend.customBackend.EmailModelBackend"]

DEFAULTS = {"USER_ID_FIELD": "id"}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "JWT_VERIFY": True,
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_SECRET_KEY": SECRET_KEY,
    "JWT_ALGORITHM": "HS256",
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "TOKEN_OBTAIN_SERIALIZER": "api.serializers.EmailPairSerializer",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "id",
} # faker.DEFAULT_PROVIDERS is loaded (all)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'epic_event_db',
        'USER': 'postgres',
        'PASSWORD': 'iwdtfw_404',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

FIXTURE_DIRS = (
   os.path.join(f"{BASE_DIR + '/api/'}", 'fixtures'),
)



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
            'verbose': {
                'format': '{levelname} {asctime}: {message}',
                'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': BASE_DIR + "/api/logs/debug.log",
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

