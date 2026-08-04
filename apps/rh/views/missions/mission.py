"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/mission/mission.py

Description :
    ViewSet des missions.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Mission,
)

from apps.rh.serializers.missions.missions import (
    MissionSerializer,
    MissionReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class MissionViewSet(
    BaseViewSet
):
    """
    ViewSet des missions.
    """

    queryset = (
        Mission.objects.all()
    )

    serializer_class = (
        MissionSerializer
    )

    read_serializer_class = (
        MissionReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "ville",
        "pays__libelle",
    )

    ordering = (
        "-date_depart",
        "-created_at",
    )

    select_related_fields = (
        "agent",
        "pays",
        "source_financement",
        "evenement",
    )