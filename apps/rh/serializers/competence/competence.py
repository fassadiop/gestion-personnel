from rest_framework import serializers

from apps.rh.models import (
    Agent,
    Competence,
    Formation,
)
from apps.rh.models.referentiels import (
    TypeCompetence,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)
from apps.rh.serializers.formation.formation import (
    FormationReadSerializer,
)
from apps.rh.serializers.referentiels.rh.type_competence import (
    TypeCompetenceReadSerializer,
)


class NiveauCompetenceSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des compétences.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    type_competence = serializers.PrimaryKeyRelatedField(
        queryset=TypeCompetence.objects.filter(actif=True)
    )

    formation = serializers.PrimaryKeyRelatedField(
        queryset=Formation.objects.filter(actif=True),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Competence

        fields = (
            "id",

            "agent",
            "type_competence",
            "formation",

            "niveau_competence",
            "date_acquisition",
            "source",
            "commentaire",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )


class NiveauCompetenceReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des compétences.
    """

    agent = AgentReadSerializer(read_only=True)

    type_competence = (
        TypeCompetenceReadSerializer(read_only=True)
    )

    formation = FormationReadSerializer(
        read_only=True
    )

    class Meta:
        model = Competence

        fields = (
            "id",

            "agent",
            "type_competence",
            "formation",

            "niveau_competence",
            "date_acquisition",
            "source",
            "commentaire",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )