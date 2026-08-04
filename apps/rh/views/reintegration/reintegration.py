
from apps.rh.models import (
    Reintegration,
)

from apps.rh.serializers.reintegration.reintegration import (
    ReintegrationSerializer,
    ReintegrationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class ReintegrationViewSet(
    BaseViewSet
):
    """
    ViewSet des réintégrations.
    """

    queryset = (
        Reintegration.objects.all()
    )

    serializer_class = (
        ReintegrationSerializer
    )

    read_serializer_class = (
        ReintegrationReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "motif",
    )

    ordering = (
        "-date_reintegration",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
    )