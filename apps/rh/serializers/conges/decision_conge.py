from rest_framework import serializers

from apps.rh.models import (
    DecisionConge,
    EvenementCarriere,
    TypeConge,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)

from apps.rh.serializers.referentiels.rh.type_conge import (
    TypeCongeReadSerializer,
)


class DecisionCongeSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création et la modification
    des décisions de congé.
    """

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(
            actif=True
        )
    )

    type_conge = serializers.PrimaryKeyRelatedField(
        queryset=TypeConge.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = DecisionConge

        fields = (
            "id",

            "evenement",
            "type_conge",

            "nombre_jours_accordes",

            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class DecisionCongeReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des décisions de congé.
    """

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    type_conge = (
        TypeCongeReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = DecisionConge

        fields = (
            "id",

            "evenement",
            "type_conge",

            "nombre_jours_accordes",

            "created_at",
            "updated_at",
        )