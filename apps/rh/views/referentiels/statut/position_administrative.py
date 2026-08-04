"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/statut/position_administrative.py

Description :
    ViewSet du référentiel des positions
    administratives.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import (
    PositionAdministrative,
)

from apps.rh.serializers.referentiels.statut.position_administrative import (
    PositionAdministrativeSerializer,
    PositionAdministrativeReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class PositionAdministrativeViewSet(
    BaseViewSet
):
    """
    ViewSet du référentiel
    PositionAdministrative.
    """

    queryset = (
        PositionAdministrative.objects.all()
    )

    serializer_class = (
        PositionAdministrativeSerializer
    )

    read_serializer_class = (
        PositionAdministrativeReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )