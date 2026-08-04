"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/evenement/type_nomination.py

Description :
    Serializers du référentiel des types
    de nomination.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeNomination

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeNominationSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    TypeNomination.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeNomination

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )


class TypeNominationReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    TypeNomination.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeNomination

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )