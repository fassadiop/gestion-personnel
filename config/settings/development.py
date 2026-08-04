"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : config/settings/development.py

Description :
    Configuration de l'environnement
    de développement.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from .base import *


# ==========================================================
# Développement
# ==========================================================

DEBUG = True


# ==========================================================
# Hôtes autorisés
# ==========================================================

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# ==========================================================
# CORS
# ==========================================================

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


# ==========================================================
# Emails
# ==========================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)