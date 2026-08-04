from apps.rh.models import (
    Disponibilite,
)

from apps.rh.serializers.disponibilite.disponibilite import (
    DisponibiliteSerializer,
    DisponibiliteReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class DisponibiliteViewSet(
    BaseViewSet
):

    queryset = (
        Disponibilite.objects.all()
    )

    serializer_class = (
        DisponibiliteSerializer
    )

    read_serializer_class = (
        DisponibiliteReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "motif",
    )

    ordering = (
        "-date_debut",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
    )