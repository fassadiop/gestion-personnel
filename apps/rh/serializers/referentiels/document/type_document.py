"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/document/type_document.py

Description :
    Serializers du référentiel des types
    de documents administratifs.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeDocument

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeDocumentSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    TypeDocument.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeDocument

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


class TypeDocumentReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    TypeDocument.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeDocument

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