from rest_framework import serializers

from apps.rh.models import Detachement
from apps.rh.serializers.agent.agent import AgentReadSerializer
from apps.rh.serializers.organisation.structure import (
    StructureReadSerializer,
)
from apps.rh.serializers.organisation.unite_organisationnelle import UniteOrganisationnelleReadSerializer


class DashboardAlerteDetachementSerializer(serializers.ModelSerializer):
    agent = AgentReadSerializer(
        source="evenement.agent",
        read_only=True,
    )

    structure = StructureReadSerializer(
        read_only=True,
    )

    unite = UniteOrganisationnelleReadSerializer(
        read_only=True,
    )

    class Meta:
        model = Detachement

        fields = (
            "id",
            "agent",
            "organisme_accueil",
            "structure",
            "unite",
            "date_debut",
            "date_fin",
        )