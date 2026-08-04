"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/statut/corps.py

Description :
    ViewSet du référentiel des corps.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import Corps

from apps.rh.serializers.referentiels.statut.corps import (
    CorpsReadSerializer,
    CorpsSerializer,
)

from apps.rh.views.base import BaseViewSet


class CorpsViewSet(BaseViewSet):
    """
    ViewSet du référentiel Corps.
    """

    queryset = Corps.objects.all()

    serializer_class = CorpsSerializer

    read_serializer_class = CorpsReadSerializer

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )