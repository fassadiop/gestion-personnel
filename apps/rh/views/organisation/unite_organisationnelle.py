"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/organisation/unite_organisationnelle.py

Description :
    ViewSet des unités organisationnelles.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.organisation import (
    UniteOrganisationnelle,
)

from apps.rh.serializers.organisation.unite_organisationnelle import (
    UniteOrganisationnelleSerializer,
    UniteOrganisationnelleReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class UniteOrganisationnelleViewSet(
    BaseViewSet
):
    """
    ViewSet des unités organisationnelles.
    """

    queryset = (
        UniteOrganisationnelle.objects.all()
    )

    serializer_class = (
        UniteOrganisationnelleSerializer
    )

    read_serializer_class = (
        UniteOrganisationnelleReadSerializer
    )

    search_fields = (
        "code",
        "nom",
        "responsable__nom",
        "responsable__prenom",
    )

    ordering = (
        "structure__nom",
        "ordre",
        "nom",
    )

    select_related_fields = (
        "structure",
        "parent",
        "type_unite",
        "responsable",
    )

    filterset_fields = (
        "structure",
        "parent",
        "type_unite",
        "responsable",
        "actif",
    )