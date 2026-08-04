from rest_framework import serializers

from apps.rh.models import Disponibilite
from apps.rh.serializers.agent.agent import AgentReadSerializer


class DashboardAlerteDisponibiliteSerializer(
    serializers.ModelSerializer
):
    agent = AgentReadSerializer(
        source="evenement.agent",
        read_only=True,
    )

    class Meta:
        model = Disponibilite

        fields = (
            "id",
            "agent",
            "motif",
            "date_debut",
            "date_fin",
        )