"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/decoration/decoration.py

Description :
    ViewSet des décorations.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Decoration,
)

from apps.rh.serializers.decoration.decoration import (
    DecorationSerializer,
    DecorationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class DecorationViewSet(
    BaseViewSet
):
    """
    ViewSet des décorations.
    """

    queryset = (
        Decoration.objects.all()
    )

    serializer_class = (
        DecorationSerializer
    )

    read_serializer_class = (
        DecorationReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "type_decoration__libelle",
        "reference_decision",
        "autorite_signataire",
    )

    ordering = (
        "-date_attribution",
        "-created_at",
    )

    select_related_fields = (
        "agent",
        "type_decoration",
        "evenement_carriere",
    )