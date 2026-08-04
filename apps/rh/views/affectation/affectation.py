"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/affectation/affectation.py

Description :
    ViewSet des affectations.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.affectation import (
    Affectation,
)

from apps.rh.serializers.affectation.affectation import (
    AffectationSerializer,
    AffectationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class AffectationViewSet(
    BaseViewSet
):
    """
    ViewSet des affectations.
    """

    queryset = (
        Affectation.objects.all()
    )

    serializer_class = (
        AffectationSerializer
    )

    read_serializer_class = (
        AffectationReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "structure__nom",
        "unite__nom",
        "poste__libelle",
    )

    ordering = (
        "-created_at",
    )

    select_related_fields = (
        "agent",
        "structure",
        "unite",
        "poste",
        "evenement",
    )