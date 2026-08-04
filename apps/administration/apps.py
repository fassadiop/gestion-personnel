"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/apps.py

Description :
    Configuration de l'application Administration.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.apps import AppConfig


class AdministrationConfig(AppConfig):
    """
    Configuration de l'application Administration.
    """

    default_auto_field = "django.db.models.BigAutoField"

    name = "apps.administration"

    verbose_name = "Administration"