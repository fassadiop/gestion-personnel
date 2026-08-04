"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/document/type_document.py

Description :
    ViewSet du référentiel des types
    de documents administratifs.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import (
    TypeDocument,
)

from apps.rh.serializers.referentiels.document.type_document import (
    TypeDocumentSerializer,
    TypeDocumentReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeDocumentViewSet(BaseViewSet):
    """
    ViewSet du référentiel TypeDocument.
    """

    queryset = TypeDocument.objects.all()

    serializer_class = (
        TypeDocumentSerializer
    )

    read_serializer_class = (
        TypeDocumentReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )