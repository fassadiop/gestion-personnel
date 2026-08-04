"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/statut/classe.py

Description :
    ViewSet du référentiel des classes.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import Classe

from apps.rh.serializers.referentiels.statut.classe import (
    ClasseSerializer,
    ClasseReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class ClasseViewSet(BaseViewSet):
    """
    ViewSet du référentiel Classe.
    """

    queryset = Classe.objects.all()

    serializer_class = ClasseSerializer

    read_serializer_class = ClasseReadSerializer

    search_fields = (
        "code",
        "libelle",
        "grade__libelle",
        "grade__corps__libelle",
    )

    ordering = (
        "grade__corps__libelle",
        "libelle",
    )

    select_related_fields = (
        "grade",
        "grade__corps",
    )