from rest_framework import serializers

from apps.rh.models import Interim
from apps.rh.serializers.agent.agent import AgentReadSerializer
from apps.rh.serializers.organisation.poste import PosteReadSerializer


class DashboardAlerteInterimSerializer(serializers.ModelSerializer):
    agent = AgentReadSerializer(
        source="evenement.agent",
        read_only=True,
    )

    poste = PosteReadSerializer(
        read_only=True,
    )

    class Meta:
        model = Interim

        fields = (
            "id",
            "agent",
            "poste",
            "date_debut",
            "date_fin",
        )