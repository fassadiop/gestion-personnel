from apps.rh.models import (
    Detachement,
)

from apps.rh.serializers.detachement.detachement import (
    DetachementSerializer,
    DetachementReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class DetachementViewSet(
    BaseViewSet
):

    queryset = (
        Detachement.objects.all()
    )

    serializer_class = (
        DetachementSerializer
    )

    read_serializer_class = (
        DetachementReadSerializer
    )

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "organisme_accueil",
        "structure__nom",
        "unite__nom",
    )

    filterset_fields = (
        "structure",
        "unite",
        "actif",
    )

    ordering = (
        "-date_debut",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
        "structure",
        "unite",
    )