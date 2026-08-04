"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/documents/document_agent.py

Description :
    ViewSet des documents des agents.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.documents import (
    DocumentAgent,
)

from rest_framework.exceptions import ValidationError

from apps.rh.serializers.agent.document_agent import (
    DocumentAgentSerializer,
    DocumentAgentReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class DocumentAgentViewSet(
    BaseViewSet
):
    """
    ViewSet des documents des agents.
    """

    queryset = (
        DocumentAgent.objects.all()
    )

    serializer_class = (
        DocumentAgentSerializer
    )

    read_serializer_class = (
        DocumentAgentReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "numero_document",
        "type_document__libelle",
    )

    ordering = (
        "agent__nom",
        "agent__prenom",
        "type_document__libelle",
    )

    select_related_fields = (
        "agent",
        "type_document",
        "verifie_par",
    )

    def perform_create(self, serializer):
        serializer.save()