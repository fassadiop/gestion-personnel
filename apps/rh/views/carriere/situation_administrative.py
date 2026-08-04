"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/carriere/situation_administrative.py

Description :
    ViewSet des situations administratives.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.carriere import (
    SituationAdministrative,
)

from apps.rh.serializers.carriere.situation_administrative import (
    SituationAdministrativeSerializer,
    SituationAdministrativeReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class SituationAdministrativeViewSet(
    BaseViewSet
):
    """
    ViewSet des situations administratives.
    """

    queryset = (
        SituationAdministrative.objects.all()
    )

    serializer_class = (
        SituationAdministrativeSerializer
    )

    read_serializer_class = (
        SituationAdministrativeReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "corps__libelle",
        "grade__libelle",
        "classe__libelle",
        "echelon__libelle",
        "position_administrative__libelle",
    )

    ordering = (
        "-date_effet",
        "-created_at",
    )

    select_related_fields = (
        "agent",
        "corps",
        "grade",
        "classe",
        "echelon",
        "position_administrative",
        "evenement",
    )