from rest_framework import serializers

from apps.rh.models import (
    Agent,
    Mission,
)
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.referentiels import (
    Pays,
    SourceFinancement,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)
from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)
from apps.rh.serializers.referentiels.geographie.pays import (
    PaysReadSerializer,
)
from apps.rh.serializers.referentiels.formation.source_financement import (
    SourceFinancementReadSerializer,
)


class MissionSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des missions.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    pays = serializers.PrimaryKeyRelatedField(
        queryset=Pays.objects.filter(actif=True)
    )

    source_financement = serializers.PrimaryKeyRelatedField(
        queryset=SourceFinancement.objects.filter(actif=True),
        allow_null=True,
        required=False,
    )

    evenement_carriere = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(actif=True)
    )

    class Meta:
        model = Mission

        fields = (
            "id",

            "agent",
            "evenement",

            "ville",
            "pays",

            "date_depart",
            "date_retour",

            "source_financement",
            "cout",

            "rapport_remis",

            "created_at",
            "updated_at",
        )


class MissionReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des missions.
    """

    agent = AgentReadSerializer(
        read_only=True
    )

    pays = PaysReadSerializer(
        read_only=True
    )

    source_financement = (
        SourceFinancementReadSerializer(
            read_only=True
        )
    )

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Mission

        fields = (
            "id",

            "agent",
            "evenement",

            "ville",
            "pays",

            "date_depart",
            "date_retour",

            "source_financement",
            "cout",

            "rapport_remis",

            "created_at",
            "updated_at",
        )