"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/carriere/recrutement.py

Description :
    ViewSet des recrutements.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Recrutement,
)

from apps.rh.serializers.recrutement.recrutement import (
    RecrutementSerializer,
    RecrutementReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class RecrutementViewSet(
    BaseViewSet
):
    """
    ViewSet des recrutements.
    """

    queryset = (
        Recrutement.objects.all()
    )

    serializer_class = (
        RecrutementSerializer
    )

    read_serializer_class = (
        RecrutementReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
    )

    ordering = (
        "-date_recrutement",
        "-created_at",
    )

    select_related_fields = (
    "evenement",
    "evenement__agent",
    "corps",
    "grade",
    "classe",
    "echelon",
    "structure",
    )