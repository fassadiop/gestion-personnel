"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/rh/type_competence.py

Description :
    ViewSet du référentiel des types
    de compétences.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeCompetence

from apps.rh.serializers.referentiels.rh.type_competence import (
    TypeCompetenceSerializer,
    TypeCompetenceReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeCompetenceViewSet(BaseViewSet):
    """
    ViewSet du référentiel TypeCompetence.
    """

    queryset = TypeCompetence.objects.all()

    serializer_class = TypeCompetenceSerializer

    read_serializer_class = (
        TypeCompetenceReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )