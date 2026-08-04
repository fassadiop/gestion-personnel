# apps/rh/views/conge_maternite/conge_maternite.py

from apps.rh.views.base import BaseViewSet

from apps.rh.models.conge_maternite import (
    CongeMaternite,
)

from apps.rh.serializers.conge_maternite.conge_maternite import (
    CongeMaterniteSerializer,
    CongeMaterniteReadSerializer,
)


class CongeMaterniteViewSet(BaseViewSet):
    """
    API de gestion des congés de maternité.
    """

    queryset = (
        CongeMaternite.objects
        .select_related(
            "evenement",
            "evenement__agent",
        )
        .all()
    )

    serializer_class = CongeMaterniteSerializer
    read_serializer_class = CongeMaterniteReadSerializer

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
    )

    filterset_fields = (
        "date_debut",
        "date_fin",
    )

    ordering = (
        "-date_debut",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
    )