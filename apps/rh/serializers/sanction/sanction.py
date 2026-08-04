from rest_framework import serializers

from apps.rh.models import (
    Agent,
    Sanction,
)
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.referentiels import (
    TypeSanction,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)
from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)
from apps.rh.serializers.referentiels.rh.type_sanction import (
    TypeSanctionReadSerializer,
)


class SanctionSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des sanctions disciplinaires.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    type_sanction = serializers.PrimaryKeyRelatedField(
        queryset=TypeSanction.objects.filter(actif=True)
    )

    evenement_carriere = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(actif=True)
    )

    class Meta:
        model = Sanction

        fields = (
            "id",

            "agent",
            "type_sanction",
            "evenement_carriere",

            "date_sanction",
            "reference_decision",
            "motif",
            "duree",
            "autorite_signataire",
            "date_fin_effet",
            "levee",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )


class SanctionReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des sanctions disciplinaires.
    """

    agent = AgentReadSerializer(
        read_only=True
    )

    type_sanction = (
        TypeSanctionReadSerializer(
            read_only=True
        )
    )

    evenement_carriere = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Sanction

        fields = (
            "id",

            "agent",
            "type_sanction",
            "evenement_carriere",

            "date_sanction",
            "reference_decision",
            "motif",
            "duree",
            "autorite_signataire",
            "date_fin_effet",
            "levee",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )