"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/evenement/statut_evenement.py

Description :
    Serializers du référentiel des statuts
    d'événements de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import StatutEvenement

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class StatutEvenementSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    StatutEvenement.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = StatutEvenement

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )


class StatutEvenementReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    StatutEvenement.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = StatutEvenement

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )