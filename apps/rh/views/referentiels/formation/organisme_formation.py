"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/formation/organisme_formation.py

Description :
    ViewSet du référentiel des organismes
    de formation.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import (
    OrganismeFormation,
)

from apps.rh.serializers.referentiels.formation.organisme_formation import (
    OrganismeFormationSerializer,
    OrganismeFormationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class OrganismeFormationViewSet(BaseViewSet):
    """
    ViewSet du référentiel OrganismeFormation.
    """

    queryset = OrganismeFormation.objects.all()

    serializer_class = (
        OrganismeFormationSerializer
    )

    read_serializer_class = (
        OrganismeFormationReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )   