"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/organisation/type_unite_organisationnelle.py

Description :
    ViewSet du référentiel des types
    d'unités organisationnelles.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.organisation import (
    TypeUniteOrganisationnelle,
)

from apps.rh.serializers.organisation.type_unite_organisationnelle import (
    TypeUniteOrganisationnelleSerializer,
    TypeUniteOrganisationnelleReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class TypeUniteOrganisationnelleViewSet(
    BaseViewSet
):
    """
    ViewSet du référentiel
    TypeUniteOrganisationnelle.
    """

    queryset = (
        TypeUniteOrganisationnelle.objects.all()
    )

    serializer_class = (
        TypeUniteOrganisationnelleSerializer
    )

    read_serializer_class = (
        TypeUniteOrganisationnelleReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )