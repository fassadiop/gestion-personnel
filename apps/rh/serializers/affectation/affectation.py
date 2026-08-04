from rest_framework import serializers

from apps.rh.models import (
    Affectation,
)
from apps.rh.models.agent import Agent
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Poste,
    Structure,
    UniteOrganisationnelle,
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
from apps.rh.serializers.organisation.structure import (
    StructureReadSerializer,
)
from apps.rh.serializers.organisation.unite_organisationnelle import (
    UniteOrganisationnelleReadSerializer,
)


class AffectationSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des affectations.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    structure = serializers.PrimaryKeyRelatedField(
        queryset=Structure.objects.filter(actif=True)
    )

    unite = serializers.PrimaryKeyRelatedField(
        queryset=UniteOrganisationnelle.objects.filter(actif=True),
        required=False,
        allow_null=True,
    )

    poste = serializers.PrimaryKeyRelatedField(
        queryset=Poste.objects.filter(actif=True),
        required=False,
        allow_null=True,
    )

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(actif=True)
    )

    class Meta:
        model = Affectation

        fields = (
            "id",

            "agent",
            "structure",
            "unite",
            "poste",
            "evenement",

            "created_at",
            "updated_at",
        )


class AffectationReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des affectations.
    """

    agent = AgentReadSerializer(read_only=True)

    structure = StructureReadSerializer(
        read_only=True
    )

    unite = (
        UniteOrganisationnelleReadSerializer(
            read_only=True
        )
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
        model = Affectation

        fields = (
            "id",

            "agent",
            "structure",
            "unite",
            "poste",
            "evenement",

            "created_at",
            "updated_at",
        )