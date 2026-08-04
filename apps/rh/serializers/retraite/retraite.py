from rest_framework import serializers

from apps.rh.models import (
    EvenementCarriere,
    Retraite,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)


class RetraiteSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des retraites.
    """

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = Retraite

        fields = (
            "id",

            "motif",

            "created_at",
            "updated_at",
        )


class RetraiteReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des retraites.
    """

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Retraite

        fields = (
            "id",

            "evenement",

            "motif",

            "created_at",
            "updated_at",
        )