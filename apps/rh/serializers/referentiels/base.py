"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/base.py

Description :
    Serializer de base des référentiels.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.serializers.base import BaseSerializer


class BaseReferentielSerializer(BaseSerializer):
    """
    Serializer de base de tous les référentiels.

    Les champs techniques sont exposés de manière
    uniforme dans toute l'application.
    """

    class Meta:
        abstract = True
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )