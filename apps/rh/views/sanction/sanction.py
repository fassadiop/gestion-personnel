"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/sanction/sanction.py

Description :
    ViewSet des sanctions.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Sanction,
)

from apps.rh.serializers.sanction.sanction import (
    SanctionSerializer,
    SanctionReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class SanctionViewSet(
    BaseViewSet
):
    """
    ViewSet des sanctions.
    """

    queryset = (
        Sanction.objects.all()
    )

    serializer_class = (
        SanctionSerializer
    )

    read_serializer_class = (
        SanctionReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "type_sanction__libelle",
        "reference_decision",
        "autorite_signataire",
    )

    ordering = (
        "-date_sanction",
        "-created_at",
    )

    select_related_fields = (
        "agent",
        "type_sanction",
        "evenement_carriere",
    )