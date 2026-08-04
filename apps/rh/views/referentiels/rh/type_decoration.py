"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/rh/type_decoration.py

Description :
    ViewSet du référentiel des types
    de décorations.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeDecoration

from apps.rh.serializers.referentiels.rh.type_decoration import (
    TypeDecorationSerializer,
    TypeDecorationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeDecorationViewSet(BaseViewSet):
    """
    ViewSet du référentiel TypeDecoration.
    """

    queryset = TypeDecoration.objects.all()

    serializer_class = TypeDecorationSerializer

    read_serializer_class = (
        TypeDecorationReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )