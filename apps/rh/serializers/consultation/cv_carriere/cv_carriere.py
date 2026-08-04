from rest_framework import serializers

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)
from apps.rh.serializers.carriere.situation_administrative import (
    SituationAdministrativeReadSerializer,
)
from apps.rh.serializers.affectation.affectation import (
    AffectationReadSerializer,
)
from apps.rh.serializers.occupation.occupation_poste import (
    OccupationPosteReadSerializer,
)

from .evenement import CVCarriereEvenementSerializer


class CVCarriereSerializer(serializers.Serializer):
    """
    Serializer de consultation du CV de carrière
    consolidé d'un agent.
    """

    agent = AgentReadSerializer(
        read_only=True
    )

    situation_administrative = (
        SituationAdministrativeReadSerializer(
            read_only=True
        )
    )

    affectation = AffectationReadSerializer(
        read_only=True
    )

    occupation = OccupationPosteReadSerializer(
        read_only=True
    )

    evenements = CVCarriereEvenementSerializer(
        many=True,
        read_only=True,
    )