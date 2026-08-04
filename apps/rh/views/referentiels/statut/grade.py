"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/statut/grade.py

Description :
    ViewSet du référentiel des grades.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import Grade

from apps.rh.serializers.referentiels.statut.grade import (
    GradeSerializer,
    GradeReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class GradeViewSet(BaseViewSet):
    """
    ViewSet du référentiel Grade.
    """

    queryset = Grade.objects.all()

    serializer_class = GradeSerializer

    read_serializer_class = GradeReadSerializer

    search_fields = (
        "code",
        "libelle",
        "corps__libelle",
    )

    ordering = (
        "corps__libelle",
        "libelle",
    )

    select_related_fields = (
        "corps",
    )