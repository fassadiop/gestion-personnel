"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/rh/type_absence.py

Description :
    ViewSet du référentiel des types
    d'absences.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeAbsence

from apps.rh.serializers.referentiels.rh.type_absence import (
    TypeAbsenceSerializer,
    TypeAbsenceReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeAbsenceViewSet(BaseViewSet):
    """
    ViewSet du référentiel TypeAbsence.
    """

    queryset = TypeAbsence.objects.all()

    serializer_class = TypeAbsenceSerializer

    read_serializer_class = (
        TypeAbsenceReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )