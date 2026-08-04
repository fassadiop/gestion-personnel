"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/evenement/type_evenement.py

Description :
    Serializers du référentiel des types
    d'événements de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeEvenement

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeEvenementSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    TypeEvenement.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeEvenement

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )


class TypeEvenementReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    TypeEvenement.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeEvenement

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )