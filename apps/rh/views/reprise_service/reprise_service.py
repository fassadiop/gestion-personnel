"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/reprise_service/reprise_service.py

Description :
    ViewSet des reprises de service.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.views.base import (
    BaseViewSet,
)

from apps.rh.models.reprise_service import (
    RepriseService,
)

from apps.rh.serializers.reprise_service.reprise_service import (
    RepriseServiceSerializer,
    RepriseServiceReadSerializer,
)


class RepriseServiceViewSet(
    BaseViewSet,
):
    """
    API de gestion des reprises de service.
    """

    queryset = (
        RepriseService.objects
        .select_related(
            "evenement",
            "evenement__agent",
        )
        .all()
    )

    serializer_class = (
        RepriseServiceSerializer
    )

    read_serializer_class = (
        RepriseServiceReadSerializer
    )

    search_fields = (

        "evenement__agent__matricule",

        "evenement__agent__nom",

        "evenement__agent__prenom",

    )

    filterset_fields = (

        "date_reprise",

    )

    ordering = (

        "-date_reprise",

        "-created_at",

    )

    select_related_fields = (

        "evenement",

        "evenement__agent",

    )