"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/geographie/pays.py

Description :
    ViewSet du référentiel des pays.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import Pays

from apps.rh.serializers.referentiels.geographie.pays import (
    PaysSerializer,
    PaysReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class PaysViewSet(BaseViewSet):
    """
    ViewSet du référentiel Pays.
    """

    queryset = Pays.objects.all()

    serializer_class = PaysSerializer

    read_serializer_class = (
        PaysReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )