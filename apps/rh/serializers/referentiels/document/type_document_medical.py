"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/document/type_document_medical.py

Description :
    Serializers du référentiel des types
    de documents médicaux.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import (
    TypeDocumentMedical,
)

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeDocumentMedicalSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    TypeDocumentMedical.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeDocumentMedical

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


class TypeDocumentMedicalReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    TypeDocumentMedical.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeDocumentMedical

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