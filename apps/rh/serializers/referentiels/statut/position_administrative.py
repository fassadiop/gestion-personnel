"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/position_administrative.py

Description :
    Serializers du référentiel des positions
    administratives.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import (
    PositionAdministrative,
)

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class PositionAdministrativeSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    PositionAdministrative.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = PositionAdministrative

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )


class PositionAdministrativeReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    PositionAdministrative.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = PositionAdministrative

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )