"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/grade.py

Description :
    Serializer du référentiel des grades.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import Grade

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.statut.corps import CorpsReadSerializer


from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class GradeSerializer(BaseReferentielSerializer):
    """
    Serializer du référentiel Grade.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = Grade

        fields = (
            "id",

            "corps",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )


class GradeReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel Grade.
    """

    corps = CorpsReadSerializer(read_only=True)

    class Meta(BaseReferentielReadSerializer.Meta):
        model = Grade

        fields = (
            "id",

            "corps",

            "code",
            "libelle",
            "description",

            "actif",

            "created_at",
            "updated_at",
        )