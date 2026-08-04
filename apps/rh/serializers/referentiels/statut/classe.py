"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/classe.py

Description :
    Serializer du référentiel des classes.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import Classe

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)

from apps.rh.serializers.referentiels.statut.grade import (
    GradeReadSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class ClasseSerializer(BaseReferentielSerializer):
    """
    Serializer du référentiel Classe.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = Classe

        fields = (
            "id",

            "grade",

            "code",
            "libelle",
            "ordre",
            "description",

            "indice_min",
            "indice_max",

            "actif",

            "created_at",
            "updated_at",
        )


class ClasseReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel Classe.
    """

    grade = GradeReadSerializer(
        read_only=True
    )

    class Meta(BaseReferentielReadSerializer.Meta):
        model = Classe

        fields = (
            "id",

            "grade",

            "code",
            "libelle",
            "ordre",
            "description",

            "indice_min",
            "indice_max",

            "actif",

            "created_at",
            "updated_at",
        )