"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/accident_travail/accident_travail.py

Description :
    ViewSet des accidents de travail.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.views.base import (
    BaseViewSet,
)

from apps.rh.models.accident_travail import (
    AccidentTravail,
)

from apps.rh.serializers.accident_travail.accident_travail import (
    AccidentTravailSerializer,
    AccidentTravailReadSerializer,
)


class AccidentTravailViewSet(
    BaseViewSet,
):
    """
    API de gestion des accidents de travail.
    """

    queryset = (
        AccidentTravail.objects
        .select_related(
            "evenement",
            "evenement__agent",
        )
        .all()
    )

    serializer_class = (
        AccidentTravailSerializer
    )

    read_serializer_class = (
        AccidentTravailReadSerializer
    )

    search_fields = (

        "evenement__agent__matricule",

        "evenement__agent__nom",

        "evenement__agent__prenom",

        "lieu_accident",

    )

    filterset_fields = (

        "date_accident",

    )

    ordering = (

        "-date_accident",

        "-created_at",

    )

    select_related_fields = (

        "evenement",

        "evenement__agent",

    )