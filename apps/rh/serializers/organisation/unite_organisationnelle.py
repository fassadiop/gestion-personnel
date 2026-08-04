from rest_framework import serializers

from apps.rh.models.agent import Agent
from apps.rh.models.organisation import (
    Structure,
    TypeUniteOrganisationnelle,
    UniteOrganisationnelle,
)

from .structure import StructureReadSerializer
from .type_unite_organisationnelle import (
    TypeUniteOrganisationnelleReadSerializer,
)


class UniteOrganisationnelleParentSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = UniteOrganisationnelle
        fields = (
            "id",
            "code",
            "sigle",
            "nom",
        )


class UniteOrganisationnelleSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des unités organisationnelles.
    """

    structure = serializers.PrimaryKeyRelatedField(
        queryset=Structure.objects.filter(actif=True)
    )

    parent = serializers.PrimaryKeyRelatedField(
        queryset=UniteOrganisationnelle.objects.filter(actif=True),
        allow_null=True,
        required=False,
    )

    type_unite = serializers.PrimaryKeyRelatedField(
        queryset=TypeUniteOrganisationnelle.objects.filter(actif=True)
    )

    responsable = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = UniteOrganisationnelle
        fields = (
            "id",
            "structure",
            "parent",
            "type_unite",
            "code",
            "sigle",
            "nom",
            "ordre",
            "responsable",
            "actif",
            "created_at",
            "updated_at",
        )


class UniteOrganisationnelleReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des unités organisationnelles.
    """

    structure = StructureReadSerializer(read_only=True)
    parent = UniteOrganisationnelleParentSerializer(
        read_only=True
    )
    type_unite = TypeUniteOrganisationnelleReadSerializer(read_only=True)
    responsable = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UniteOrganisationnelle
        fields = (
            "id",
            "structure",
            "parent",
            "type_unite",
            "code",
            "sigle",
            "nom",
            "ordre",
            "responsable",
            "actif",
            "created_at",
            "updated_at",
        )