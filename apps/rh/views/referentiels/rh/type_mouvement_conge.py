"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/rh/type_mouvement_conge.py

Description :
    ViewSet des types de mouvements
    de congé.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    TypeMouvementConge,
)

from apps.rh.serializers.referentiels.rh.type_mouvement_conge import (
    TypeMouvementCongeSerializer,
    TypeMouvementCongeReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeMouvementCongeViewSet(
    BaseViewSet
):
    """
    ViewSet des types de mouvements
    de congé.
    """

    queryset = (
        TypeMouvementConge.objects.all()
    )

    serializer_class = (
        TypeMouvementCongeSerializer
    )

    read_serializer_class = (
        TypeMouvementCongeReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
        "description",
    )

    filterset_fields = (
        "sens",
        "actif",
    )

    ordering = (
        "libelle",
    )

    select_related_fields = ()