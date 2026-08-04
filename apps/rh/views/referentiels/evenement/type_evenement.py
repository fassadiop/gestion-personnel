"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/evenement/type_evenement.py

Description :
    ViewSet du référentiel des types
    d'événements de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import (
    TypeEvenement,
)

from apps.rh.serializers.referentiels.evenement.type_evenement import (
    TypeEvenementSerializer,
    TypeEvenementReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeEvenementViewSet(BaseViewSet):
    """
    ViewSet du référentiel TypeEvenement.
    """

    queryset = TypeEvenement.objects.all()

    serializer_class = (
        TypeEvenementSerializer
    )

    read_serializer_class = (
        TypeEvenementReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )