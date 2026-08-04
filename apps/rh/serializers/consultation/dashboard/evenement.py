from rest_framework import serializers

from apps.rh.models import EvenementCarriere
from apps.rh.serializers.agent.agent import AgentReadSerializer
from apps.rh.serializers.referentiels.evenement.statut_evenement import (
    StatutEvenementReadSerializer,
)
from apps.rh.serializers.referentiels.evenement.type_evenement import (
    TypeEvenementReadSerializer,
)


class DashboardEvenementSerializer(serializers.ModelSerializer):
    agent = AgentReadSerializer(read_only=True)

    type_evenement = TypeEvenementReadSerializer(
        read_only=True,
    )

    statut = StatutEvenementReadSerializer(
        read_only=True,
    )

    class Meta:
        model = EvenementCarriere

        fields = (
            "id",
            "agent",
            "type_evenement",
            "statut",
            "date_effet",
        )