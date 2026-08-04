from rest_framework import serializers
from apps.rh.models.absence import Absence
from apps.rh.models.referentiels import TypeAbsence
from apps.rh.serializers.agent.agent import AgentReadSerializer
from apps.rh.serializers.evenement.evenement import EvenementCarriereReadSerializer
from apps.rh.serializers.referentiels.rh.type_absence import TypeAbsenceReadSerializer


class AbsenceSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des absences.
    """

    type_absence = serializers.PrimaryKeyRelatedField(
        queryset=TypeAbsence.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = Absence

        fields = (
            "id",

            "type_absence",

            "date_debut",

            "date_fin",

            "jours_deductibles",

            "motif",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class AbsenceReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des absences.
    """

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    agent = AgentReadSerializer(
        source="evenement.agent",
        read_only=True,
    )

    type_absence = (
        TypeAbsenceReadSerializer(
            read_only=True
        )
    )

    nombre_jours = serializers.ReadOnlyField()

    class Meta:
        model = Absence

        fields = (
            "id",

            "evenement",

            "agent",

            "type_absence",

            "date_debut",

            "date_fin",

            "nombre_jours",

            "jours_deductibles",

            "motif",

            "created_at",

            "updated_at",
        )