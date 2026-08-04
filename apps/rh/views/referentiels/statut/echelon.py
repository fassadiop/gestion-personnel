"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/statut/echelon.py

Description :
    ViewSet du référentiel des échelons.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import Echelon

from apps.rh.serializers.referentiels.statut.echelon import (
    EchelonSerializer,
    EchelonReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class EchelonViewSet(BaseViewSet):
    """
    ViewSet du référentiel Échelon.
    """

    queryset = Echelon.objects.all()

    serializer_class = EchelonSerializer

    read_serializer_class = EchelonReadSerializer

    search_fields = (
        "code",
        "libelle",
        "classe__libelle",
        "classe__grade__libelle",
        "classe__grade__corps__libelle",
    )

    ordering = (
        "classe__grade__corps__libelle",
        "classe__grade__libelle",
        "classe__ordre",
        "ordre",
        "libelle",
    )

    select_related_fields = (
        "classe",
        "classe__grade",
        "classe__grade__corps",
    )