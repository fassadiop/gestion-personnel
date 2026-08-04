"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/occupation/occupation_poste.py

Description :
    ViewSet des occupations de postes.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.occupation import (
    OccupationPoste,
)

from apps.rh.serializers.occupation.occupation_poste import (
    OccupationPosteSerializer,
    OccupationPosteReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class OccupationPosteViewSet(
    BaseViewSet
):
    """
    ViewSet des occupations de postes.
    """

    queryset = (
        OccupationPoste.objects.all()
    )

    serializer_class = (
        OccupationPosteSerializer
    )

    read_serializer_class = (
        OccupationPosteReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "poste__libelle",
    )

    ordering = (
        "-date_debut",
        "-created_at",
    )

    select_related_fields = (
        "agent",
        "poste",
        "evenement",
    )