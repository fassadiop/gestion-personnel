"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/conges/conge.py

Description :
    ViewSet des congés.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Conge,
)

from apps.rh.serializers.conges.conge import (
    CongeSerializer,
    CongeReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class CongeViewSet(
    BaseViewSet
):
    """
    ViewSet des congés.
    """

    queryset = (
        Conge.objects.all()
    )

    serializer_class = (
        CongeSerializer
    )

    read_serializer_class = (
        CongeReadSerializer
    )

    search_fields = (
        "decision_conge__evenement__agent__matricule",
        "decision_conge__evenement__agent__nom",
        "decision_conge__evenement__agent__prenom",
        "decision_conge__type_conge__libelle",
        "decision_conge__evenement__reference_acte",
    )

    filterset_fields = (
        "decision_conge",
        "decision_conge__type_conge",
        "actif",
    )

    ordering = (
        "-date_cessation_service",
        "-created_at",
    )

    select_related_fields = (
        "decision_conge",
        "decision_conge__evenement",
        "decision_conge__evenement__agent",
        "decision_conge__type_conge",
    )