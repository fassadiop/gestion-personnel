"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/rh/type_absence.py

Description :
    Serializers du référentiel des types
    d'absences.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeAbsence

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeAbsenceSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    TypeAbsence.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeAbsence

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


class TypeAbsenceReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    TypeAbsence.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeAbsence

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