from apps.rh.models.referentiels import (
    SourceFinancement,
)

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class SourceFinancementSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    SourceFinancement.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = SourceFinancement

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )


class SourceFinancementReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    SourceFinancement.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = SourceFinancement

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )