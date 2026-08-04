"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/corps.py

Description :
    Serializer du référentiel des corps.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import Corps
from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import BaseReferentielReadSerializer
from apps.rh.serializers.referentiels.statut.hierarchie import HierarchieReadSerializer


class CorpsSerializer(BaseReferentielSerializer):
    """
    Serializer du référentiel Corps.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = Corps

        fields = (
            "id",
            "hierarchie",
            "code",
            "libelle",
            "description",
            "actif",
            "created_at",
            "updated_at",
        )


class CorpsReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel Corps.
    """

    hierarchie = HierarchieReadSerializer(read_only=True)

    class Meta(BaseReferentielReadSerializer.Meta):
        model = Corps

        fields = (
            "id",

            "code",
            "hierarchie",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )