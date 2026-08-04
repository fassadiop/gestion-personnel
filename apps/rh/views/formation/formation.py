"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/formation/formation.py

Description :
    ViewSet des formations.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Formation,
)

from apps.rh.serializers.formation.formation import (
    FormationSerializer,
    FormationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class FormationViewSet(
    BaseViewSet
):
    """
    ViewSet des formations.
    """

    queryset = (
        Formation.objects.all()
    )

    serializer_class = (
        FormationSerializer
    )

    read_serializer_class = (
        FormationReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "intitule",
        "organisme_formation__libelle",
        "type_formation__libelle",
    )

    ordering = (
        "-date_debut",
        "-created_at",
    )

    select_related_fields = (
        "agent",
        "type_formation",
        "organisme_formation",
        "pays",
        "source_financement",
        "evenement_carriere",
    )