"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/agent/agent.py

Description :
    ViewSet des agents.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import Agent

from apps.rh.serializers.agent.agent import (
    AgentSerializer,
    AgentReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class AgentViewSet(BaseViewSet):
    """
    ViewSet des agents.
    """

    queryset = Agent.objects.all()

    serializer_class = AgentSerializer

    read_serializer_class = AgentReadSerializer

    search_fields = (
        "matricule",
        "nom",
        "prenom",
        "telephone",
        "email",
    )

    ordering = (
        "nom",
        "prenom",
    )

    select_related_fields = (
        "statut",
        "sexe",
        "nationalite",
        "etat_civil",
    )