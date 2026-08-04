"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/conges/compteur_conge.py

Description :
    ViewSet des compteurs de congé.

Auteur : SGCP
Version : 1.0
==========================================================
"""



from apps.rh.models.compteur_conge import CompteurConge
from apps.rh.serializers.conges.compteur_conge import (
    CompteurCongeSerializer,
    CompteurCongeReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class CompteurCongeViewSet(
    BaseViewSet
):
    """
    ViewSet des compteurs de congé.
    """

    queryset = (
        CompteurConge.objects.all()
    )

    serializer_class = (
        CompteurCongeSerializer
    )

    read_serializer_class = (
        CompteurCongeReadSerializer
    )

    search_fields = (
        "decision_conge__evenement__agent__matricule",
        "decision_conge__evenement__agent__nom",
        "decision_conge__evenement__agent__prenom",
        "decision_conge__type_conge__libelle",
        "decision_conge__evenement__reference_acte",
    )

    filterset_fields = (
        "decision_conge__type_conge",
        "actif",
    )

    ordering = (
        "-decision_conge__evenement__date_effet",
        "-created_at",
    )

    select_related_fields = (
        "decision_conge",
        "decision_conge__evenement",
        "decision_conge__evenement__agent",
        "decision_conge__type_conge",
    )