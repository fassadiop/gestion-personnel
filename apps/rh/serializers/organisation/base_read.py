"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/organisation/base_read.py

Description :
    Classe de base des serializers
    de lecture du domaine Organisation.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.serializers.base_read import (
    BaseReadSerializer,
)


class BaseOrganisationReadSerializer(
    BaseReadSerializer
):
    """
    Classe de base des serializers
    de lecture du domaine Organisation.
    """

    class Meta(BaseReadSerializer.Meta):
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )