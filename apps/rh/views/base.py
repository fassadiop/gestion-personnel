"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/base.py

Description :
    ViewSet de base du SGCP.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.db.models import QuerySet

from django_filters.rest_framework import (
    DjangoFilterBackend,
)

from rest_framework import filters
from rest_framework import viewsets

from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
    JSONParser,
)

from apps.rh.core.pagination import SGCPPagination
from apps.rh.core.permissions import IsAuthenticatedAndActive


class BaseViewSet(viewsets.ModelViewSet):
    """
    ViewSet de base du SGCP.

    Tous les ViewSets du projet héritent
    de cette classe.
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

    ordering = (
        "-created_at",
    )

    filterset_fields = ()

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    select_related_fields = ()

    prefetch_related_fields = ()

    def get_queryset(self):
        """
        Optimise automatiquement les requêtes.
        """

        queryset = super().get_queryset()

        if not isinstance(queryset, QuerySet):
            return queryset

        if self.select_related_fields:
            queryset = queryset.select_related(
                *self.select_related_fields
            )

        if self.prefetch_related_fields:
            queryset = queryset.prefetch_related(
                *self.prefetch_related_fields
            )

        return queryset

    def get_serializer_class(self):
        """
        Retourne automatiquement
        le serializer approprié.
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