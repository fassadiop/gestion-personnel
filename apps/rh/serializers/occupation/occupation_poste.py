from rest_framework import serializers

from apps.rh.models import (
    Agent,
    EvenementCarriere,
    OccupationPoste,
    Poste,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)

from apps.rh.serializers.organisation.poste import (
    PosteReadSerializer,
)


class OccupationPosteSerializer(serializers.ModelSerializer):

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    poste = serializers.PrimaryKeyRelatedField(
        queryset=Poste.objects.filter(actif=True)
    )

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(actif=True)
    )

    class Meta:

        model = OccupationPoste

        fields = (
            "id",

            "agent",
            "poste",
            "evenement",

            "date_debut",
            "date_fin",

            "est_interim",

            "actif",

            "created_at",
            "updated_at",
        )

    def validate(self, attrs):

        agent = attrs.get("agent")
        poste = attrs.get("poste")
        date_debut = attrs.get("date_debut")
        date_fin = attrs.get("date_fin")

        if (
            date_fin
            and
            date_fin < date_debut
        ):
            raise serializers.ValidationError(
                {
                    "date_fin":
                    (
                        "La date de fin doit être "
                        "postérieure à la date de début."
                    )
                }
            )

        queryset = OccupationPoste.objects.filter(
            poste=poste,
            date_fin__isnull=True,
        )

        if self.instance:
            queryset = queryset.exclude(
                pk=self.instance.pk
            )

        if queryset.exists():
            raise serializers.ValidationError(
                {
                    "poste":
                    (
                        "Ce poste est déjà occupé."
                    )
                }
            )

        queryset = OccupationPoste.objects.filter(
            agent=agent,
            date_fin__isnull=True,
        )

        if self.instance:
            queryset = queryset.exclude(
                pk=self.instance.pk
            )

        if queryset.exists():
            raise serializers.ValidationError(
                {
                    "agent":
                    (
                        "Cet agent occupe déjà un poste."
                    )
                }
            )

        return attrs


class OccupationPosteReadSerializer(
    serializers.ModelSerializer
):

    agent = AgentReadSerializer(
        read_only=True
    )

    poste = PosteReadSerializer(
        read_only=True
    )

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:

        model = OccupationPoste

        fields = (

            "id",

            "agent",

            "poste",

            "evenement",

            "date_debut",
            "date_fin",

            "est_interim",

            "actif",

            "created_at",
            "updated_at",

        )