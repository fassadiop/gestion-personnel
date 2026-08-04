from apps.rh.models import (
    FinInterim,
)

from apps.rh.serializers.fin_interim.fin_interim import (
    FinInterimSerializer,
    FinInterimReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class FinInterimViewSet(
    BaseViewSet
):

    queryset = (
        FinInterim.objects.all()
    )

    serializer_class = (
        FinInterimSerializer
    )

    read_serializer_class = (
        FinInterimReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
    )

    ordering = (
        "-date_fin_interim",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
    )