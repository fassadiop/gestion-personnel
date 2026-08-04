from rest_framework import serializers

from apps.rh.models import (
    Agent,
    Evaluation,
    UniteOrganisationnelle,
)
from apps.rh.models.evenement import EvenementCarriere

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)
from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)
from apps.rh.serializers.organisation.unite_organisationnelle import (
    UniteOrganisationnelleReadSerializer,
)


class EvaluationSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des évaluations.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    evaluateur = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    unite_organisationnelle = serializers.PrimaryKeyRelatedField(
        queryset=UniteOrganisationnelle.objects.filter(actif=True)
    )

    evenement_carriere = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(actif=True),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Evaluation

        fields = (
            "id",

            "agent",
            "evaluateur",
            "unite_organisationnelle",
            "evenement_carriere",

            "annee",
            "date_evaluation",
            "note_globale",

            "appreciation_generale",
            "points_forts",
            "points_a_ameliorer",
            "besoins_formation",
            "perspectives_carriere",

            "recommandation_avancement",
            "recommandation_promotion",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )


class EvaluationReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des évaluations.
    """

    agent = AgentReadSerializer(read_only=True)

    evaluateur = AgentReadSerializer(read_only=True)

    unite_organisationnelle = (
        UniteOrganisationnelleReadSerializer(
            read_only=True
        )
    )

    evenement_carriere = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Evaluation

        fields = (
            "id",

            "agent",
            "evaluateur",
            "unite_organisationnelle",
            "evenement_carriere",

            "annee",
            "date_evaluation",
            "note_globale",

            "appreciation_generale",
            "points_forts",
            "points_a_ameliorer",
            "besoins_formation",
            "perspectives_carriere",

            "recommandation_avancement",
            "recommandation_promotion",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )