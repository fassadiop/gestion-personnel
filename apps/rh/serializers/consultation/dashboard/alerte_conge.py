from rest_framework import serializers

from apps.rh.models import Conge
from apps.rh.serializers.agent.agent import AgentReadSerializer
from apps.rh.serializers.conges.decision_conge import DecisionCongeReadSerializer



class DashboardAlerteCongeSerializer(
    serializers.ModelSerializer
):
    agent = AgentReadSerializer(
        read_only=True,
    )

    decision_conge = DecisionCongeReadSerializer(
        read_only=True,
    )

    class Meta:
        model = Conge

        fields = (
            "id",
            "agent",
            "decision_conge",
            "date_cessation_service",
            "date_reprise",
        )