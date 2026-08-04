# apps/rh/serializers/referentiels/hierarchie.py

from apps.rh.models.referentiels import Hierarchie
from apps.rh.serializers.referentiels.base import BaseReferentielSerializer
from apps.rh.serializers.referentiels.base_read import BaseReferentielReadSerializer


class HierarchieSerializer(BaseReferentielSerializer):

    class Meta(BaseReferentielSerializer.Meta):
        model = Hierarchie

        fields = (
            "id",
            "code",
            "libelle",
            "abreviation",
            "ordre",
            "description",
            "actif",
            "created_at",
            "updated_at",
        )


class HierarchieReadSerializer(BaseReferentielReadSerializer):

    class Meta(BaseReferentielReadSerializer.Meta):
        model = Hierarchie

        fields = (
            "id",
            "code",
            "libelle",
            "abreviation",
            "ordre",
            "description",
            "actif",
            "created_at",
            "updated_at",
        )