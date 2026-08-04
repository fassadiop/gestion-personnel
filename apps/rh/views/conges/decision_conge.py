"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/conges/decision_conge.py

Description :
    ViewSet des décisions de congé.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    DecisionConge,
)

from apps.rh.serializers.conges.decision_conge import (
    DecisionCongeSerializer,
    DecisionCongeReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class DecisionCongeViewSet(
    BaseViewSet
):
    """
    ViewSet des décisions de congé.
    """

    queryset = (
        DecisionConge.objects.all()
    )

    serializer_class = (
        DecisionCongeSerializer
    )

    read_serializer_class = (
        DecisionCongeReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "evenement__reference_acte",
        "type_conge__libelle",
    )

    filterset_fields = (
        "type_conge",
        "actif",
    )

    ordering = (
        "-evenement__date_effet",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
        "type_conge",
    )

    def get_queryset(self):
        """
        Filtre les décisions de congé
        selon les paramètres de recherche.
        """

        queryset = super().get_queryset()

        agent = self.request.query_params.get(
            "agent",
        )

        if agent:

            queryset = queryset.filter(
                evenement__agent_id=agent,
            )

        return queryset