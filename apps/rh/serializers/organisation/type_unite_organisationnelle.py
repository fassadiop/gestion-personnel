from apps.rh.models.organisation import TypeUniteOrganisationnelle

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeUniteOrganisationnelleSerializer(
    BaseReferentielSerializer
):
    """
    Serializer utilisé pour la création et la modification
    des types d'unités organisationnelles.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeUniteOrganisationnelle

        fields = (
            "id",
            "code",
            "libelle",
            "description",
            "actif",
            "created_at",
            "updated_at",
        )


class TypeUniteOrganisationnelleReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer utilisé pour la consultation
    des types d'unités organisationnelles.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeUniteOrganisationnelle

        fields = (
            "id",
            "code",
            "libelle",
            "description",
            "actif",
            "created_at",
            "updated_at",
        )