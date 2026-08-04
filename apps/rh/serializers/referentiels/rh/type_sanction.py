"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/rh/type_sanction.py

Description :
    Serializers du référentiel des types
    de sanctions.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeSanction

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeSanctionSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    TypeSanction.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeSanction

        fields = (
            # Identifiant
            "id",

            # Identification
            "code",
            "libelle",

            # Métier
            "niveau",

            # Description
            "description",

            # État
            "actif",

            # Audit
            "created_at",
            "updated_at",
        )


class TypeSanctionReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    TypeSanction.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeSanction

        fields = (
            # Identifiant
            "id",

            # Identification
            "code",
            "libelle",

            # Métier
            "niveau",

            # Description
            "description",

            # État
            "actif",

            # Audit
            "created_at",
            "updated_at",
        )