"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/conge_maladie/conge_maladie.py

Description :
    ViewSet des congés de maladie.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.conge_maladie import (
    CongeMaladie,
)

from apps.rh.serializers.conge_maladie.conge_maladie import (
    CongeMaladieSerializer,
    CongeMaladieReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class CongeMaladieViewSet(
    BaseViewSet
):
    """
    ViewSet des congés de maladie.
    """

    queryset = (
        CongeMaladie.objects.all()
    )

    serializer_class = (
        CongeMaladieSerializer
    )

    read_serializer_class = (
        CongeMaladieReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
    )

    ordering = (
        "-debut_conge",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
    )