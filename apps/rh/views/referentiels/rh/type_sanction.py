"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/rh/type_sanction.py

Description :
    ViewSet du référentiel des types
    de sanctions.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeSanction

from apps.rh.serializers.referentiels.rh.type_sanction import (
    TypeSanctionSerializer,
    TypeSanctionReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeSanctionViewSet(BaseViewSet):
    """
    ViewSet du référentiel TypeSanction.
    """

    queryset = TypeSanction.objects.all()

    serializer_class = TypeSanctionSerializer

    read_serializer_class = (
        TypeSanctionReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )