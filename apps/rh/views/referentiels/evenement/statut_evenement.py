"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/evenement/statut_evenement.py

Description :
    ViewSet du référentiel des statuts
    d'événements de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import (
    StatutEvenement,
)

from apps.rh.serializers.referentiels.evenement.statut_evenement import (
    StatutEvenementSerializer,
    StatutEvenementReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class StatutEvenementViewSet(BaseViewSet):
    """
    API du référentiel des statuts
    d'événements de carrière.
    """

    queryset = (
        StatutEvenement.objects.all()
    )

    serializer_class = (
        StatutEvenementSerializer
    )

    read_serializer_class = (
        StatutEvenementReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
        "description",
    )

    ordering_fields = (
        "code",
        "libelle",
        "created_at",
    )

    ordering = (
        "libelle",
    )