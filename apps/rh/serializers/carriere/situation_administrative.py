from rest_framework import serializers

from apps.rh.models import Agent
from apps.rh.models.carriere import SituationAdministrative
from apps.rh.models.referentiels import (
    Corps,
    Grade,
    Classe,
    Echelon,
    PositionAdministrative,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)
from apps.rh.serializers.referentiels.statut.corps import (
    CorpsReadSerializer,
)
from apps.rh.serializers.referentiels.statut.grade import (
    GradeReadSerializer,
)
from apps.rh.serializers.referentiels.statut.classe import (
    ClasseReadSerializer,
)
from apps.rh.serializers.referentiels.statut.echelon import (
    EchelonReadSerializer,
)
from apps.rh.serializers.referentiels.statut.position_administrative import (
    PositionAdministrativeReadSerializer,
)


class SituationAdministrativeSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des situations administratives.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    corps = serializers.PrimaryKeyRelatedField(
        queryset=Corps.objects.filter(actif=True)
    )

    grade = serializers.PrimaryKeyRelatedField(
        queryset=Grade.objects.filter(actif=True)
    )

    classe = serializers.PrimaryKeyRelatedField(
        queryset=Classe.objects.filter(actif=True)
    )

    echelon = serializers.PrimaryKeyRelatedField(
        queryset=Echelon.objects.filter(actif=True)
    )

    position_administrative = serializers.PrimaryKeyRelatedField(
        queryset=PositionAdministrative.objects.filter(actif=True)
    )

    class Meta:
        model = SituationAdministrative

        fields = (
            "id",
            "agent",
            "corps",
            "grade",
            "classe",
            "echelon",
            "position_administrative",
            "date_effet",
            "date_fin",
            "evenement",
            "actif",
            "created_at",
            "updated_at",
        )


class SituationAdministrativeReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des situations administratives.
    """

    agent = AgentReadSerializer(read_only=True)
    corps = CorpsReadSerializer(read_only=True)
    grade = GradeReadSerializer(read_only=True)
    classe = ClasseReadSerializer(read_only=True)
    echelon = EchelonReadSerializer(read_only=True)
    position_administrative = (
        PositionAdministrativeReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = SituationAdministrative

        fields = (
            "id",
            "agent",
            "corps",
            "grade",
            "classe",
            "echelon",
            "position_administrative",
            "date_effet",
            "date_fin",
            "evenement",
            "actif",
            "created_at",
            "updated_at",
        )