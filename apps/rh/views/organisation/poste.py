"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/organisation/poste.py

Description :
    ViewSet des postes.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.organisation import (
    Poste,
)

from apps.rh.serializers.organisation.poste import (
    PosteSerializer,
    PosteReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class PosteViewSet(BaseViewSet):
    """
    ViewSet des postes.
    """

    queryset = Poste.objects.all()

    serializer_class = (
        PosteSerializer
    )

    read_serializer_class = (
        PosteReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
        "unite__nom",
    )

    ordering = (
        "structure__nom",
        "unite__nom",
        "libelle",
    )

    select_related_fields = (
        "structure",
        "unite",
        "hierarchie_minimale",
    )

    filterset_fields = (
        "structure",
        "unite",
        "est_responsable",
        "est_budgetise",
        "actif",
    )