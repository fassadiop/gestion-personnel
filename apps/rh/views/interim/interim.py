from apps.rh.models import (
    Interim,
)

from apps.rh.serializers.interim.interim import (
    InterimReadSerializer,
    InterimSerializer,
)

from apps.rh.views.base import BaseViewSet


class InterimViewSet(BaseViewSet):

    queryset = Interim.objects.all()

    serializer_class = InterimSerializer

    read_serializer_class = InterimReadSerializer

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "poste__libelle",
    )

    ordering = (
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
        "poste",
    )