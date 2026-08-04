"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/medical/document_medical.py

Description :
    ViewSet des documents médicaux.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    DocumentMedical,
)

from apps.rh.serializers.medical.document_medical import (
    DocumentMedicalSerializer,
    DocumentMedicalReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class DocumentMedicalViewSet(
    BaseViewSet
):
    """
    ViewSet des documents médicaux.
    """

    queryset = (
        DocumentMedical.objects.all()
    )

    serializer_class = (
        DocumentMedicalSerializer
    )

    read_serializer_class = (
        DocumentMedicalReadSerializer
    )

    search_fields = (
        "dossier_medical__agent__matricule",
        "dossier_medical__agent__nom",
        "dossier_medical__agent__prenom",
        "numero_document",
        "type_document__libelle",
    )

    ordering = (
        "-date_document",
        "-created_at",
    )

    select_related_fields = (
        "dossier_medical",
        "dossier_medical__agent",
        "type_document",
    )