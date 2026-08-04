"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/competence/niveau_competence.py

Description :
    ViewSet des niveaux de compétences.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    NiveauCompetence,
)

from apps.rh.serializers.competence.competence import (
    NiveauCompetenceSerializer,
    NiveauCompetenceReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class NiveauCompetenceViewSet(
    BaseViewSet
):
    """
    ViewSet des niveaux de compétences.
    """

    queryset = (
        NiveauCompetence.objects.all()
    )

    serializer_class = (
        NiveauCompetenceSerializer
    )

    read_serializer_class = (
        NiveauCompetenceReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "type_competence__libelle",
        "niveau",
    )

    ordering = (
        "agent__nom",
        "agent__prenom",
        "type_competence__libelle",
    )

    select_related_fields = (
        "agent",
        "type_competence",
        "formation",
    )