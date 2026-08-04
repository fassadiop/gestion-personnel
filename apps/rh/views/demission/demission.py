"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/demission.py

Description :
    ViewSet des démissions.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models import (
    Demission,
)

from apps.rh.serializers.demission.demission import (
    DemissionSerializer,
    DemissionReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class DemissionViewSet(
    BaseViewSet
):
    """
    ViewSet des démissions.
    """

    queryset = (
        Demission.objects.all()
    )

    serializer_class = (
        DemissionSerializer
    )

    read_serializer_class = (
        DemissionReadSerializer
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