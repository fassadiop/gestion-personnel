"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/rh/type_decoration.py

Description :
    Serializers du référentiel des types
    de décorations.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeDecoration

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeDecorationSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    TypeDecoration.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeDecoration

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


class TypeDecorationReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    TypeDecoration.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeDecoration

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