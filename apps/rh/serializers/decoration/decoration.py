from rest_framework import serializers

from apps.rh.models import (
    Agent,
    Decoration,
)
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.referentiels import TypeDecoration

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)
from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)
from apps.rh.serializers.referentiels.rh.type_decoration import (
    TypeDecorationReadSerializer,
)


class DecorationSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des décorations.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    type_decoration = serializers.PrimaryKeyRelatedField(
        queryset=TypeDecoration.objects.filter(actif=True)
    )

    evenement_carriere = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(actif=True)
    )

    class Meta:
        model = Decoration

        fields = (
            "id",

            "agent",
            "type_decoration",
            "evenement_carriere",

            "date_attribution",
            "reference_decision",
            "autorite_signataire",
            "motif",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )


class DecorationReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des décorations.
    """

    agent = AgentReadSerializer(read_only=True)

    type_decoration = (
        TypeDecorationReadSerializer(read_only=True)
    )

    evenement_carriere = (
        EvenementCarriereReadSerializer(read_only=True)
    )

    class Meta:
        model = Decoration

        fields = (
            "id",

            "agent",
            "type_decoration",
            "evenement_carriere",

            "date_attribution",
            "reference_decision",
            "autorite_signataire",
            "motif",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )