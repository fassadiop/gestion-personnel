"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/rh/type_conge.py

Description :
    ViewSet du référentiel des types
    de congés.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeConge

from apps.rh.serializers.referentiels.rh.type_conge import (
    TypeCongeSerializer,
    TypeCongeReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeCongeViewSet(BaseViewSet):
    """
    ViewSet du référentiel TypeConge.
    """

    queryset = TypeConge.objects.all()

    serializer_class = TypeCongeSerializer

    read_serializer_class = (
        TypeCongeReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )