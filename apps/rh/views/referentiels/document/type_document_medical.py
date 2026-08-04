"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/document/type_document_medical.py

Description :
    ViewSet du référentiel des types
    de documents médicaux.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import (
    TypeDocumentMedical,
)

from apps.rh.serializers.referentiels.document.type_document_medical import (
    TypeDocumentMedicalSerializer,
    TypeDocumentMedicalReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeDocumentMedicalViewSet(BaseViewSet):
    """
    ViewSet du référentiel TypeDocumentMedical.
    """

    queryset = TypeDocumentMedical.objects.all()

    serializer_class = (
        TypeDocumentMedicalSerializer
    )

    read_serializer_class = (
        TypeDocumentMedicalReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )