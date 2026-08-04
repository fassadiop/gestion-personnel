"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/conges/mouvement_compteur_conge.py

Description :
    ViewSet des mouvements de compteur
    de congé.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.mouvement_compteur_conge import MouvementCompteurConge
from apps.rh.serializers.conges.mouvement_compteur_conge import (
    MouvementCompteurCongeSerializer,
    MouvementCompteurCongeReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class MouvementCompteurCongeViewSet(
    BaseViewSet
):
    """
    ViewSet des mouvements de compteur
    de congé.
    """

    queryset = (
        MouvementCompteurConge.objects.all()
    )

    serializer_class = (
        MouvementCompteurCongeSerializer
    )

    read_serializer_class = (
        MouvementCompteurCongeReadSerializer
    )

    search_fields = (
        "compteur__decision_conge__evenement__agent__matricule",
        "compteur__decision_conge__evenement__agent__nom",
        "compteur__decision_conge__evenement__agent__prenom",
        "compteur__decision_conge__evenement__reference_acte",
        "type_mouvement__code",
        "type_mouvement__libelle",
        "observation",
    )

    filterset_fields = (
        "compteur",
        "type_mouvement",
        "date_mouvement",
        "actif",
    )

    ordering = (
        "-date_mouvement",
        "-created_at",
    )

    select_related_fields = (
        "compteur",
        "compteur__decision_conge",
        "compteur__decision_conge__evenement",
        "compteur__decision_conge__evenement__agent",
        "compteur__decision_conge__type_conge",
        "type_mouvement",
    )