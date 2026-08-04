"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/radiation.py

Description :
    ViewSet des radiations.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models import (
    Radiation,
)

from apps.rh.serializers.radiation.radiation import (
    RadiationSerializer,
    RadiationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class RadiationViewSet(
    BaseViewSet
):
    """
    ViewSet des radiations.
    """

    queryset = (
        Radiation.objects.all()
    )

    serializer_class = (
        RadiationSerializer
    )

    read_serializer_class = (
        RadiationReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "motif",
    )

    ordering = (
        "-id",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
    )