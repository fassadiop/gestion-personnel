from rest_framework import serializers

from apps.rh.models import (
    Demission,
    EvenementCarriere,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)


class DemissionSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des démissions.
    """

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = Demission

        fields = (
            "id",

            "motif",

            "created_at",
            "updated_at",
        )


class DemissionReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des démissions.
    """

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Demission

        fields = (
            "id",

            "evenement",

            "motif",

            "created_at",
            "updated_at",
        )