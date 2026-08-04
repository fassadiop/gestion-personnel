"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/organisation/structure.py

Description :
    ViewSet des structures administratives.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.organisation import (
    Structure,
)

from apps.rh.serializers.organisation.structure import (
    StructureSerializer,
    StructureReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class StructureViewSet(BaseViewSet):
    """
    ViewSet des structures administratives.
    """

    queryset = Structure.objects.all()

    serializer_class = (
        StructureSerializer
    )

    read_serializer_class = (
        StructureReadSerializer
    )

    search_fields = (
        "code",
        "nom",
        "sigle",
        "email",
        "telephone",
    )

    ordering = (
        "nom",
    )

    select_related_fields = (
        "type_structure",
        "parent",
    )

    filterset_fields = (
        "type_structure",
        "parent",
        "actif",
    )