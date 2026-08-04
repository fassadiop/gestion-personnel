"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/carriere/nomination.py

Description :
    ViewSet des nominations.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Nomination,
)

from apps.rh.serializers.nomination.nomination import (
    NominationSerializer,
    NominationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class NominationViewSet(
    BaseViewSet
):
    """
    ViewSet des nominations.
    """

    queryset = (
        Nomination.objects.all()
    )

    serializer_class = (
        NominationSerializer
    )

    read_serializer_class = (
        NominationReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "poste__libelle",
        "structure__nom",
        "unite__nom",
        "evenement__reference_acte",
        "evenement__objet",
    )

    ordering = (
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
        "structure",
        "unite",
        "poste",
    )