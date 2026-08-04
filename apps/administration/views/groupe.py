"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/views/groupe.py

Description :
    ViewSet de gestion des groupes
    (rôles fonctionnels).

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth.models import Group
from apps.administration.views.base import BaseAdministrationViewSet

from apps.administration.serializers.groupe import (
    GroupeSerializer,
    GroupeReadSerializer,
    GroupeDetailSerializer,
)


class GroupeViewSet(BaseAdministrationViewSet):
    """
    Gestion des rôles fonctionnels.
    """

    queryset = (
        Group.objects
        .prefetch_related(
            "permissions",
            "user_set",
        )
        .all()
    )

    serializer_class = GroupeSerializer

    read_serializer_class = (
        GroupeReadSerializer
    )

    detail_serializer_class = (
        GroupeDetailSerializer
    )

    search_fields = (
        "name",
    )

    ordering_fields = (
        "name",
    )