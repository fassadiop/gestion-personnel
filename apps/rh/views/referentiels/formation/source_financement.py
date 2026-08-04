"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/formation/source_financement.py

Description :
    ViewSet du référentiel des sources
    de financement.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import (
    SourceFinancement,
)

from apps.rh.serializers.referentiels.formation.source_financement import (
    SourceFinancementSerializer,
    SourceFinancementReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class SourceFinancementViewSet(BaseViewSet):
    """
    ViewSet du référentiel SourceFinancement.
    """

    queryset = SourceFinancement.objects.all()

    serializer_class = (
        SourceFinancementSerializer
    )

    read_serializer_class = (
        SourceFinancementReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )