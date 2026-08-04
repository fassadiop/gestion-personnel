"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/carriere/titularisation.py

Description :
    ViewSet des titularisations.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models import (
    Titularisation,
)

from apps.rh.serializers.titularisation.titularisation import (
    TitularisationSerializer,
    TitularisationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TitularisationViewSet(
    BaseViewSet
):
    """
    ViewSet des titularisations.
    """

    queryset = (
        Titularisation.objects.all()
    )

    serializer_class = (
        TitularisationSerializer
    )

    read_serializer_class = (
        TitularisationReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
    )

    ordering = (
        "-id",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
        "position_administrative",
        "grade",
        "classe",
        "echelon",
    )