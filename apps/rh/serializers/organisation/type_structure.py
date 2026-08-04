from rest_framework import serializers

from apps.rh.models import TypeStructure

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeStructureSerializer(
    BaseReferentielSerializer
):
    """
    Serializer utilisé pour la création et la modification
    des types de structure.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeStructure

        fields = (
            "id",
            "code",
            "libelle",
            "description",
            "actif",
            "created_at",
            "updated_at",
        )


class TypeStructureReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer utilisé pour la lecture des types de structure.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeStructure

        fields = (
            "id",
            "code",
            "libelle",
            "description",
            "actif",
            "created_at",
            "updated_at",
        )