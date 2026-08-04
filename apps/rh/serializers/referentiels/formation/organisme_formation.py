"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/formation/organisme_formation.py

Description :
    Serializers du référentiel des organismes
    de formation.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import (
    OrganismeFormation,
)

from apps.rh.serializers.referentiels.base import (
    BaseReferentielSerializer,
)
from apps.rh.serializers.referentiels.base_read import (
    BaseReferentielReadSerializer,
)


class OrganismeFormationSerializer(
    BaseReferentielSerializer
):
    """
    Serializer d'écriture du référentiel
    OrganismeFormation.
    """

    class Meta(BaseReferentielSerializer.Meta):
        model = OrganismeFormation

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


class OrganismeFormationReadSerializer(
    BaseReferentielReadSerializer
):
    """
    Serializer de lecture du référentiel
    OrganismeFormation.
    """

    class Meta(BaseReferentielReadSerializer.Meta):
        model = OrganismeFormation

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