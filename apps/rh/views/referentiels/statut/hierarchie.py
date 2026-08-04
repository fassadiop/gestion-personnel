# apps/rh/views/referentiels/statut/hierarchie.py

from apps.rh.models.referentiels import Hierarchie

from apps.rh.serializers.referentiels.statut.hierarchie import (
    HierarchieSerializer,
    HierarchieReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class HierarchieViewSet(BaseViewSet):

    queryset = Hierarchie.objects.all()

    serializer_class = HierarchieSerializer

    read_serializer_class = HierarchieReadSerializer

    search_fields = (
        "code",
        "libelle",
        "abreviation",
    )

    ordering_fields = (
        "ordre",
        "code",
        "libelle",
    )

    ordering = (
        "ordre",
    )