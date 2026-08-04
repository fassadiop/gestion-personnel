from rest_framework import serializers

from apps.rh.models import (
    Agent,
    Mutation,
)
from apps.rh.models.evenement import EvenementCarriere

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)
from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)


class MutationSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des mutations.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(actif=True)
    )

    class Meta:
        model = Mutation

        fields = (
            "id",

            "agent",
            "evenement",

            "structure",
            "unite",
            "poste",

            "created_at",
            "updated_at",
        )


class MutationReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des mutations.
    """

    agent = AgentReadSerializer(
        read_only=True
    )

    evenement_carriere = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Mutation

        fields = (
            "id",
            
            "agent",
            "evenement",

            "structure",
            "unite",
            "poste",

            "created_at",
            "updated_at",
        )