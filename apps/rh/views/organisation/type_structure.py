"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/organisation/type_structure.py

Description :
    ViewSet du référentiel des types
    de structures.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.organisation import (
    TypeStructure,
)

from apps.rh.serializers.organisation.type_structure import (
    TypeStructureSerializer,
    TypeStructureReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeStructureViewSet(BaseViewSet):
    """
    ViewSet du référentiel TypeStructure.
    """

    queryset = TypeStructure.objects.all()

    serializer_class = (
        TypeStructureSerializer
    )

    read_serializer_class = (
        TypeStructureReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )