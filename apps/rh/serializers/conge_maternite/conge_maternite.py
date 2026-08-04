# apps/rh/serializers/conge_maternite/conge_maternite.py

from rest_framework import serializers

from apps.rh.models.conge_maternite import (
    CongeMaternite,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)


class CongeMaterniteSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la création
    et la modification des congés
    de maternité.
    """

    class Meta:
        model = CongeMaternite

        fields = (
            "id",

            "date_debut",

            "date_fin",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class CongeMaterniteReadSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la consultation
    des congés de maternité.
    """

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True,
        )
    )

    agent = AgentReadSerializer(
        source="evenement.agent",
        read_only=True,
    )

    nombre_jours = serializers.ReadOnlyField()

    class Meta:
        model = CongeMaternite

        fields = (
            "id",

            "evenement",

            "agent",

            "date_debut",

            "date_fin",

            "nombre_jours",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )