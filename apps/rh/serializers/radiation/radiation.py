from rest_framework import serializers

from apps.rh.models import (
    EvenementCarriere,
    Radiation,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)


class RadiationSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des radiations.
    """

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = Radiation

        fields = (
            "id",

            "motif",

            "created_at",
            "updated_at",
        )


class RadiationReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des radiations.
    """

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Radiation

        fields = (
            "id",

            "evenement",

            "motif",

            "created_at",
            "updated_at",
        )