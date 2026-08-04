"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/documents/document_administratif.py

Description :
    ViewSet des documents administratifs.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.documents import (
    DocumentAdministratif,
)

from apps.rh.serializers.documents.documents import (
    DocumentSerializer,
    DocumentReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class DocumentAdministratifViewSet(
    BaseViewSet
):
    """
    ViewSet des documents administratifs.
    """

    queryset = (
        DocumentAdministratif.objects.all()
    )

    serializer_class = (
        DocumentSerializer
    )

    read_serializer_class = (
        DocumentReadSerializer
    )

    search_fields = (
        "numero_document",
        "signataire",
        "type_document__libelle",
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
    )

    ordering = (
        "-date_document",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
        "type_document",
        "structure_emettrice",
    )