from rest_framework import serializers

from apps.rh.models import (
    Disponibilite,
    EvenementCarriere,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)


class DisponibiliteSerializer(
    serializers.ModelSerializer
):

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = Disponibilite

        fields = (
            "id",
            "evenement",
            "motif",
            "date_debut",
            "date_fin",
            "created_at",
            "updated_at",
        )


class DisponibiliteReadSerializer(
    serializers.ModelSerializer
):

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Disponibilite

        fields = (
            "id",
            "evenement",
            "motif",
            "date_debut",
            "date_fin",
            "created_at",
            "updated_at",
        )