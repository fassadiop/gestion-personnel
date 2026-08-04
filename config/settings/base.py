"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : config/settings/base.py

Description :
    Configuration commune à tous les
    environnements (développement,
    recette, production).

Auteur : SGCP
Version : 1.0
==========================================================
"""

from datetime import timedelta
from pathlib import Path


# ==========================================================
# Répertoires du projet
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent


# ==========================================================
# Sécurité
# ==========================================================

SECRET_KEY = (
    "django-insecure-"
    "nzpsgypl*gfe4xp%*f$^tk3("
    "*ow#x_x6t@%6b(=n+%*4i)ek@7"
)


# ==========================================================
# Applications Django
# ==========================================================

DJANGO_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

]


# ==========================================================
# Applications tierces
# ==========================================================

THIRD_PARTY_APPS = [

    "rest_framework",

    "drf_spectacular",

    "django_filters",

    "corsheaders",

    "rest_framework_simplejwt.token_blacklist",

]


# ==========================================================
# Applications SGCP
# ==========================================================

LOCAL_APPS = [

    "apps.rh.apps.RhConfig",

    "apps.authentication.apps.AuthenticationConfig",

    "apps.administration.apps.AdministrationConfig",

]


INSTALLED_APPS = (
    DJANGO_APPS
    + THIRD_PARTY_APPS
    + LOCAL_APPS
)


# ==========================================================
# Middleware
# ==========================================================

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


# ==========================================================
# URLS
# ==========================================================

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"


# ==========================================================
# Templates
# ==========================================================

TEMPLATES = [

    {

        "BACKEND":
            "django.template.backends.django.DjangoTemplates",

        "DIRS": [],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]


# ==========================================================
# Base de données
# ==========================================================

DATABASES = {

    "default": {

        "ENGINE": "django.db.backends.postgresql",

        "NAME": "saas_sgcp",

        "USER": "olga",

        "PASSWORD": "Olga2974",

        "HOST": "localhost",

        "PORT": "5432",

    },

}


# ==========================================================
# Validation des mots de passe
# ==========================================================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation."
        "MinimumLengthValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation."
        "CommonPasswordValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation."
        "NumericPasswordValidator",
    },

]


# ==========================================================
# Internationalisation
# ==========================================================

LANGUAGE_CODE = "fr"

TIME_ZONE = "Africa/Dakar"

USE_I18N = True

USE_TZ = True


# ==========================================================
# Fichiers statiques
# ==========================================================

STATIC_URL = "/static/"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ==========================================================
# Clé primaire par défaut
# ==========================================================

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)


# ==========================================================
# Django REST Framework
# ==========================================================

REST_FRAMEWORK = {

    # Authentification
    "DEFAULT_AUTHENTICATION_CLASSES": (

        "rest_framework_simplejwt.authentication."
        "JWTAuthentication",

    ),

    # Permissions
    "DEFAULT_PERMISSION_CLASSES": (

        "apps.rh.core.permissions."
        "IsAuthenticatedAndActive",

    ),

    # Pagination
    "DEFAULT_PAGINATION_CLASS":
        "apps.rh.core.pagination.SGCPPagination",

    "PAGE_SIZE": 20,

    # Recherche / Filtres / Tri
    "DEFAULT_FILTER_BACKENDS": (

        "django_filters.rest_framework."
        "DjangoFilterBackend",

        "rest_framework.filters.SearchFilter",

        "rest_framework.filters.OrderingFilter",

    ),

    # Parsing
    "DEFAULT_PARSER_CLASSES": (

        "rest_framework.parsers.JSONParser",

        "rest_framework.parsers.FormParser",

        "rest_framework.parsers.MultiPartParser",

    ),

    # Rendu
    "DEFAULT_RENDERER_CLASSES": (

        "rest_framework.renderers.JSONRenderer",

    ),

    # Format des dates
    "DATE_FORMAT": "%d/%m/%Y",

    "DATETIME_FORMAT": "%d/%m/%Y %H:%M",

    # Formats d'entrée
    "DATE_INPUT_FORMATS": (

        "%Y-%m-%d",

        "%d/%m/%Y",

    ),

    "DATETIME_INPUT_FORMATS": (

        "%Y-%m-%d %H:%M:%S",

        "%d/%m/%Y %H:%M",

    ),

    # Gestion des exceptions
    "EXCEPTION_HANDLER":
        "rest_framework.views.exception_handler",

    # Documentation OpenAPI
    "DEFAULT_SCHEMA_CLASS":
        "drf_spectacular.openapi.AutoSchema",

}


# ==========================================================
# Documentation OpenAPI
# ==========================================================

SPECTACULAR_SETTINGS = {

    "TITLE":
        "SGCP API",

    "DESCRIPTION":
        (
            "API du Système de Gestion "
            "de Carrière du Personnel"
        ),

    "VERSION":
        "1.0.0",

    "SERVE_INCLUDE_SCHEMA":
        False,

    "COMPONENT_SPLIT_REQUEST":
        True,

}


# ==========================================================
# JSON Web Token
# ==========================================================

SIMPLE_JWT = {

    "ACCESS_TOKEN_LIFETIME":
        timedelta(hours=8),

    "REFRESH_TOKEN_LIFETIME":
        timedelta(days=7),

    "ROTATE_REFRESH_TOKENS":
        True,

    "BLACKLIST_AFTER_ROTATION":
        True,

    "UPDATE_LAST_LOGIN":
        True,

    "ALGORITHM":
        "HS256",

    "SIGNING_KEY":
        SECRET_KEY,

    "AUTH_HEADER_TYPES": (

        "Bearer",

    ),

    "AUTH_TOKEN_CLASSES": (

        "rest_framework_simplejwt.tokens.AccessToken",

    ),

    "TOKEN_TYPE_CLAIM":
        "token_type",

    "JTI_CLAIM":
        "jti",

}