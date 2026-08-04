"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/rh/type_formation.py

Description :
    Serializers du référentiel des types
    de formations.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeFormation

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeFormationSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    TypeFormation.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeFormation

        fields = (
            # Identifiant
            "id",

            # Identification
            "code",
            "libelle",

            # Description
            "description",

            # État
            "actif",

            # Audit
            "created_at",
            "updated_at",
        )


class TypeFormationReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    TypeFormation.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeFormation

        fields = (
            # Identifiant
            "id",

            # Identification
            "code",
            "libelle",

            # Description
            "description",

            # État
            "actif",

            # Audit
            "created_at",
            "updated_at",
        )