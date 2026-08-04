"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/carriere/mutation.py

Description :
    ViewSet des mutations.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Mutation,
)

from apps.rh.serializers.mutation.mutation import (
    MutationSerializer,
    MutationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class MutationViewSet(
    BaseViewSet
):
    """
    ViewSet des mutations.
    """

    queryset = (
        Mutation.objects.all()
    )

    serializer_class = (
        MutationSerializer
    )

    read_serializer_class = (
        MutationReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "ancienne_structure__nom",
        "nouvelle_structure__nom",
        "ancien_poste__libelle",
        "nouveau_poste__libelle",
    )

    ordering = (
        "-date_effet",
        "-created_at",
    )

    select_related_fields = (
        "agent",
        "ancienne_structure",
        "nouvelle_structure",
        "ancienne_unite",
        "nouvelle_unite",
        "ancien_poste",
        "nouveau_poste",
        "evenement_carriere",
    )