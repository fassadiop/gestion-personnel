from rest_framework import serializers

from apps.rh.models import Formation
from apps.rh.models import Agent
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.referentiels import (
    OrganismeFormation,
    Pays,
    SourceFinancement,
    TypeFormation,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)
from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)
from apps.rh.serializers.referentiels.formation.organisme_formation import (
    OrganismeFormationReadSerializer,
)
from apps.rh.serializers.referentiels.formation.source_financement import SourceFinancementReadSerializer
from apps.rh.serializers.referentiels.geographie.pays import (
    PaysReadSerializer,
)
from apps.rh.serializers.referentiels.rh.type_formation import (
    TypeFormationReadSerializer,
)


class FormationSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des formations.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    type_formation = serializers.PrimaryKeyRelatedField(
        queryset=TypeFormation.objects.filter(actif=True)
    )

    organisme_formation = serializers.PrimaryKeyRelatedField(
        queryset=OrganismeFormation.objects.filter(actif=True)
    )

    pays = serializers.PrimaryKeyRelatedField(
        queryset=Pays.objects.filter(actif=True)
    )

    source_financement = serializers.PrimaryKeyRelatedField(
        queryset=SourceFinancement.objects.filter(actif=True),
        allow_null=True,
        required=False,
    )

    evenement_carriere = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(actif=True)
    )

    class Meta:
        model = Formation

        fields = (
            "id",

            "agent",
            "type_formation",
            "organisme_formation",
            "pays",
            "source_financement",
            "evenement_carriere",

            "intitule",
            "date_debut",
            "date_fin",

            "cout",

            "rapport_depose",
            "diplome_obtenu",
            "numero_diplome",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )


class FormationReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des formations.
    """

    agent = AgentReadSerializer(read_only=True)

    type_formation = TypeFormationReadSerializer(
        read_only=True
    )

    organisme_formation = (
        OrganismeFormationReadSerializer(
            read_only=True
        )
    )

    pays = PaysReadSerializer(read_only=True)

    source_financement = (
        SourceFinancementReadSerializer(
            read_only=True
        )
    )

    evenement_carriere = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Formation

        fields = (
            "id",

            "agent",
            "type_formation",
            "organisme_formation",
            "pays",
            "source_financement",
            "evenement_carriere",

            "intitule",
            "date_debut",
            "date_fin",

            "cout",

            "rapport_depose",
            "diplome_obtenu",
            "numero_diplome",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )