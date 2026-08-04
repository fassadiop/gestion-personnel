from apps.rh.models import (
    PriseServiceAffectation,
)

from apps.rh.serializers.prise_service_affectation.prise_service_affectation import (
    PriseServiceAffectationSerializer,
    PriseServiceAffectationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class PriseServiceAffectationViewSet(
    BaseViewSet
):

    queryset = (
        PriseServiceAffectation.objects.all()
    )

    serializer_class = (
        PriseServiceAffectationSerializer
    )

    read_serializer_class = (
        PriseServiceAffectationReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "structure__nom",
        "unite__nom",
    )

    filterset_fields = (
        "structure",
        "unite",
        "actif",
    )

    ordering = (
        "-date_prise_service",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
        "structure",
        "unite",
    )