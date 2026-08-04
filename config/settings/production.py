"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : config/settings/production.py

Description :
    Configuration de l'environnement
    de production.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from .base import *


# ==========================================================
# Production
# ==========================================================

DEBUG = False


# ==========================================================
# Hôtes autorisés
# ==========================================================

ALLOWED_HOSTS = [
    "sgcp.gouv.sn",
]


# ==========================================================
# Sécurité
# ==========================================================

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True


# ==========================================================
# Emails
# ==========================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.smtp.EmailBackend"
)