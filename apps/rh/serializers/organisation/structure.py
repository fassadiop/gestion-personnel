from rest_framework import serializers

from apps.rh.models.organisation import (
    Structure,
    TypeStructure,
)

from .type_structure import (
    TypeStructureReadSerializer,
)


class StructureSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des structures administratives.
    """

    type_structure = serializers.PrimaryKeyRelatedField(
        queryset=TypeStructure.objects.filter(actif=True)
    )

    parent = serializers.PrimaryKeyRelatedField(
        queryset=Structure.objects.filter(actif=True),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Structure

        fields = (
            "id",
            "type_structure",
            "parent",
            "code",
            "nom",
            "sigle",
            "telephone",
            "email",
            "adresse",
            "site_web",
            "date_creation",
            "actif",
            "created_at",
            "updated_at",
        )


class StructureReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des structures administratives.
    """

    type_structure = TypeStructureReadSerializer(
        read_only=True
    )

    parent = serializers.SerializerMethodField()

    class Meta:
        model = Structure

        fields = (
            "id",
            "type_structure",
            "parent",
            "code",
            "nom",
            "sigle",
            "telephone",
            "email",
            "adresse",
            "site_web",
            "date_creation",
            "actif",
            "created_at",
            "updated_at",
        )

    def get_parent(self, obj):
        """
        Retourne les informations essentielles de la
        structure parente.
        """
        if obj.parent is None:
            return None

        return {
            "id": obj.parent.id,
            "code": obj.parent.code,
            "sigle": obj.parent.sigle,
            "nom": obj.parent.nom,
        }