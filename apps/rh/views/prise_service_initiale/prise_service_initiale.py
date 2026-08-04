"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/prise_service_initiale.py

Description :
    ViewSet des prises de service initiales.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    PriseServiceInitiale,
)

from apps.rh.serializers.prise_service_initiale.prise_service_initiale import (
    PriseServiceInitialeSerializer,
    PriseServiceInitialeReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class PriseServiceInitialeViewSet(
    BaseViewSet
):
    """
    ViewSet des prises de service initiales.
    """

    queryset = (
        PriseServiceInitiale.objects.all()
    )

    serializer_class = (
        PriseServiceInitialeSerializer
    )

    read_serializer_class = (
        PriseServiceInitialeReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "structure__nom",
        "unite__nom",
    )

    filterset_fields = (
        "structure",
        "unite",
        "actif",
    )

    ordering = (
        "-date_prise_service",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
        "structure",
        "unite",
    )