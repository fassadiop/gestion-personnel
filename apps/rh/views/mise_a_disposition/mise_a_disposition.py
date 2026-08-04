"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/mise_a_disposition.py

Description :
    ViewSet des mises à disposition.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    MiseADisposition,
)

from apps.rh.serializers.mise_a_disposition.mise_a_disposition import (
    MiseADispositionSerializer,
    MiseADispositionReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class MiseADispositionViewSet(
    BaseViewSet
):
    """
    ViewSet des mises à disposition.
    """

    queryset = (
        MiseADisposition.objects.all()
    )

    serializer_class = (
        MiseADispositionSerializer
    )

    read_serializer_class = (
        MiseADispositionReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "organisme_accueil",
        "structure__nom",
        "unite__nom",
    )

    filterset_fields = (
        "structure",
        "unite",
        "actif",
    )

    ordering = (
        "-date_debut",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
        "structure",
        "unite",
    )