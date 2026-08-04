from rest_framework import serializers

from apps.rh.serializers.referentiels.statut.classe import ClasseReadSerializer
from apps.rh.serializers.referentiels.statut.echelon import EchelonReadSerializer
from apps.rh.serializers.referentiels.statut.grade import GradeReadSerializer
from apps.rh.serializers.referentiels.statut.position_administrative import PositionAdministrativeReadSerializer

from apps.rh.models import (
    Titularisation,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)

class TitularisationSerializer(
    serializers.ModelSerializer
):
    """
    Serializer de création/modification.
    """

    class Meta:
        model = Titularisation

        fields = (
            "id",

            "evenement",

            "position_administrative",

            "grade",

            "classe",

            "echelon",

            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class TitularisationReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer de consultation.
    """

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    position_administrative = (
        PositionAdministrativeReadSerializer(
            read_only=True
        )
    )

    grade = (
        GradeReadSerializer(
            read_only=True
        )
    )

    classe = (
        ClasseReadSerializer(
            read_only=True
        )
    )

    echelon = (
        EchelonReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Titularisation

        fields = (
            "id",

            "evenement",

            "position_administrative",

            "grade",

            "classe",

            "echelon",

            "created_at",
            "updated_at",
        )