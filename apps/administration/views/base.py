"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/views/base.py

Description :
    ViewSet de base du module Administration.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django_filters.rest_framework import (
    DjangoFilterBackend,
)

from rest_framework import filters
from rest_framework import viewsets

from rest_framework.parsers import (
    FormParser,
    JSONParser,
    MultiPartParser,
)

from apps.rh.core.pagination import (
    SGCPPagination,
)
from apps.rh.core.permissions import (
    IsAuthenticatedAndActive,
)


class BaseAdministrationViewSet(
    viewsets.ModelViewSet,
):
    """
    ViewSet de base du module Administration.
    """

    parser_classes = (
        MultiPartParser,
        FormParser,
        JSONParser,
    )

    permission_classes = (
        IsAuthenticatedAndActive,
    )

    pagination_class = SGCPPagination

    serializer_class = None

    read_serializer_class = None

    detail_serializer_class = None

    search_fields = ()

    ordering_fields = "__all__"

    filterset_fields = ()

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    def get_serializer_class(self):
        """
        Retourne automatiquement
        le serializer adapté
        à l'action courante.
        """

        if (
            self.action == "retrieve"
            and self.detail_serializer_class
        ):
            return self.detail_serializer_class

        if (
            self.action == "list"
            and self.read_serializer_class
        ):
            return self.read_serializer_class

        return self.serializer_class

    def get_read_serializer(
        self,
        *args,
        **kwargs,
    ):
        """
        Retourne le serializer de lecture.
        """

        serializer_class = (
            self.read_serializer_class
            or self.serializer_class
        )

        kwargs.setdefault(
            "context",
            self.get_serializer_context(),
        )

        return serializer_class(
            *args,
            **kwargs,
        )

    def perform_create(
        self,
        serializer,
    ):
        """
        Création d'un objet.
        """

        serializer.save()

    def perform_update(
        self,
        serializer,
    ):
        """
        Modification d'un objet.
        """

        serializer.save()

    def perform_destroy(
        self,
        instance,
    ):
        """
        Suppression d'un objet.
        """

        instance.delete()