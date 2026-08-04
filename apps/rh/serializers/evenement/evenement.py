from rest_framework import serializers

from apps.rh.models import Agent
from apps.rh.models.evenement import (
    EvenementCarriere,
)
from apps.rh.models.referentiels import (
    PositionAdministrative,
    StatutEvenement,
    TypeEvenement,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)
from apps.rh.serializers.referentiels.evenement.statut_evenement import (
    StatutEvenementReadSerializer,
)
from apps.rh.serializers.referentiels.evenement.type_evenement import (
    TypeEvenementReadSerializer,
)
from apps.rh.serializers.referentiels.statut.position_administrative import (
    PositionAdministrativeReadSerializer,
)

from apps.rh.services.creation.creation import (
    EvenementCreationService,
)


class EvenementCarriereSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des événements de carrière.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    type_evenement = serializers.PrimaryKeyRelatedField(
        queryset=TypeEvenement.objects.filter(actif=True)
    )

    position_administrative = serializers.PrimaryKeyRelatedField(
        queryset=PositionAdministrative.objects.filter(actif=True),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = EvenementCarriere

        fields = (
            "id",

            "agent",
            "type_evenement",
            "position_administrative",

            "date_effet",
            "date_fin",

            "reference_acte",
            "objet",
            "description",
            "observation",

            "actif",

            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )

    def _get_creation_payload(self):
        """
        Retourne le payload transmis
        au moteur de création.
        """

        return self.initial_data

    def create(
        self,
        validated_data,
    ):
        """
        Crée un événement de carrière
        via le moteur de création.
        """

        request = self.context.get(
            "request"
        )

        utilisateur = (
            request.user
            if request
            else None
        )

        service = (
            EvenementCreationService()
        )

        statut_en_attente = (
            StatutEvenement.objects.get(
                code="EN_ATTENTE"
            )
        )

        validated_data["statut"] = statut_en_attente

        return service.creer(

            validated_data=validated_data,

            payload=self._get_creation_payload(),

            utilisateur=utilisateur,

            request=request,
        )


class EvenementCarriereReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des événements de carrière.
    """

    agent = AgentReadSerializer(
        read_only=True
    )

    type_evenement = TypeEvenementReadSerializer(
        read_only=True
    )

    position_administrative = (
        PositionAdministrativeReadSerializer(
            read_only=True
        )
    )

    statut = StatutEvenementReadSerializer(
        read_only=True
    )

    class Meta:
        model = EvenementCarriere

        fields = (
            "id",

            "agent",
            "type_evenement",
            "statut",
            "position_administrative",

            "date_effet",
            "date_fin",

            "reference_acte",
            "objet",
            "description",
            "observation",

            "actif",

            "created_at",
            "updated_at",
        )