"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/geographie/pays.py

Description :
    Serializers du référentiel des pays.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import Pays

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class PaysSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel Pays.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = Pays

        fields = (
            # Identifiant
            "id",

            # Identification
            "code",
            "libelle",

            # Description
            "description",

            # État
            "actif",

            # Audit
            "created_at",
            "updated_at",
        )


class PaysReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel Pays.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = Pays

        fields = (
            # Identifiant
            "id",

            # Identification
            "code",
            "libelle",

            # Description
            "description",

            # État
            "actif",

            # Audit
            "created_at",
            "updated_at",
        )