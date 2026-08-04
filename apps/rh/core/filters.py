"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : core/filters.py

Description :
    Filtres communs du SGCP.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django_filters import rest_framework as filters


class BaseFilterSet(filters.FilterSet):
    """
    Classe de base des filtres du SGCP.
    """

    pass