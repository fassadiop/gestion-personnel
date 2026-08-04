"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/base_read.py

Description :
    Classe de base des serializers de lecture.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.serializers.base import BaseSerializer


class BaseReadSerializer(BaseSerializer):
    """
    Classe de base des serializers utilisés
    pour les opérations de lecture (GET).

    Elle permet d'harmoniser les serializers
    de consultation tout en laissant la logique
    métier aux serializers spécialisés.
    """

    pass