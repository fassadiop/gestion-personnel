"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/retraite.py

Description :
    ViewSet des retraites.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models import (
    Retraite,
)

from apps.rh.serializers.retraite.retraite import (
    RetraiteSerializer,
    RetraiteReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class RetraiteViewSet(
    BaseViewSet
):
    """
    ViewSet des retraites.
    """

    queryset = (
        Retraite.objects.all()
    )

    serializer_class = (
        RetraiteSerializer
    )

    read_serializer_class = (
        RetraiteReadSerializer
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