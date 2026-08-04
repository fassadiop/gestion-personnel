"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/rh/type_competence.py

Description :
    Serializers du référentiel des types
    de compétences.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeCompetence

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeCompetenceSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    TypeCompetence.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeCompetence

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


class TypeCompetenceReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    TypeCompetence.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeCompetence

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