"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/rh/type_formation.py

Description :
    ViewSet du référentiel des types
    de formations.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeFormation

from apps.rh.serializers.referentiels.rh.type_formation import (
    TypeFormationSerializer,
    TypeFormationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeFormationViewSet(BaseViewSet):
    """
    ViewSet du référentiel TypeFormation.
    """

    queryset = TypeFormation.objects.all()

    serializer_class = TypeFormationSerializer

    read_serializer_class = (
        TypeFormationReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )