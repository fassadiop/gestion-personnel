"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/base_read.py

Description :
    Classe de base des serializers de lecture
    des référentiels.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.serializers.base_read import (
    BaseReadSerializer,
)


class BaseReferentielReadSerializer(
    BaseReadSerializer
):
    """
    Classe de base des serializers de lecture
    des référentiels.
    """

    class Meta:
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )