"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/rh/type_conge.py

Description :
    Serializers du référentiel des types
    de congés.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import TypeConge

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class TypeCongeSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    TypeConge.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = TypeConge

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "duree_par_defaut",
            "fractionnement_autorise",
            "justificatif_obligatoire",
            "impacte_compteur",

            "actif",

            "created_at",
            "updated_at",
        )


class TypeCongeReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    TypeConge.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = TypeConge

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "duree_par_defaut",
            "fractionnement_autorise",
            "justificatif_obligatoire",
            "impacte_compteur",

            "actif",

            "created_at",
            "updated_at",
        )