from rest_framework import serializers

from apps.rh.models import (
    EvenementCarriere,
    Reintegration,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)


class ReintegrationSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des réintégrations.
    """

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = Reintegration

        fields = (
            "id",
            "evenement",
            "motif",
            "date_reintegration",
            "created_at",
            "updated_at",
        )


class ReintegrationReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des réintégrations.
    """

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Reintegration

        fields = (
            "id",
            "evenement",
            "motif",
            "date_reintegration",
            "created_at",
            "updated_at",
        )