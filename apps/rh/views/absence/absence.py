"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/absence/absence.py

Description :
    ViewSet des absences.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Absence,
)

from apps.rh.serializers.absence.absence import (
    AbsenceSerializer,
    AbsenceReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class AbsenceViewSet(
    BaseViewSet
):
    """
    ViewSet des absences.
    """

    queryset = (
        Absence.objects.all()
    )

    serializer_class = (
        AbsenceSerializer
    )

    read_serializer_class = (
        AbsenceReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "type_absence__libelle",
        "motif",
    )

    filterset_fields = (
        "type_absence",
    )

    ordering = (
        "-date_debut",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
        "type_absence",
    )