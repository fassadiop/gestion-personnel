from rest_framework import serializers

from apps.rh.models import (
    EvenementCarriere,
    FinInterim,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)


class FinInterimSerializer(
    serializers.ModelSerializer
):

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = FinInterim

        fields = (
            "id",
            "evenement",
            "date_fin_interim",
            "created_at",
            "updated_at",
        )


class FinInterimReadSerializer(
    serializers.ModelSerializer
):

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = FinInterim

        fields = (
            "id",
            "evenement",
            "date_fin_interim",
            "created_at",
            "updated_at",
        )