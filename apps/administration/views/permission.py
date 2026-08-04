"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/views/permission.py

Description :
    ViewSet de consultation des permissions.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth.models import Permission

from apps.administration.views.base import BaseAdministrationViewSet

from apps.administration.serializers.permission import (
    PermissionSerializer,
    PermissionReadSerializer,
)


class PermissionViewSet(BaseAdministrationViewSet):
    """
    Gestion des permissions.
    """

    queryset = (
        Permission.objects
        .select_related(
            "content_type",
        )
        .all()
    )

    serializer_class = (
        PermissionSerializer
    )

    read_serializer_class = (
        PermissionReadSerializer
    )

    search_fields = (
        "name",
        "codename",
        "content_type__app_label",
        "content_type__model",
    )

    ordering_fields = (
        "content_type__app_label",
        "content_type__model",
        "codename",
    )

    filterset_fields = (
        "content_type__app_label",
        "content_type__model",
    )