"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/echelon.py

Description :
    Serializer du référentiel des échelons.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import Echelon

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)


from apps.rh.serializers.referentiels.statut.classe import (
    ClasseReadSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class EchelonSerializer(BaseReferentielSerializer):
    """
    Serializer du référentiel Échelon.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = Echelon

        fields = (
            "id",

            "classe",

            "code",
            "libelle",

            "ordre",
            "indice",

            "description",

            "actif",

            "created_at",
            "updated_at",
        )


class EchelonReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel Échelon.
    """

    classe = ClasseReadSerializer(
        read_only=True
    )

    class Meta(BaseReferentielReadSerializer.Meta):
        model = Echelon

        fields = (
            "id",

            "classe",

            "code",
            "libelle",

            "ordre",
            "indice",

            "description",

            "actif",

            "created_at",
            "updated_at",
        )