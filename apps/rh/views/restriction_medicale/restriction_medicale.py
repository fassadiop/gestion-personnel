"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/restriction_medicale/restriction_medicale.py

Description :
    ViewSet des restrictions médicales.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.views.base import (
    BaseViewSet,
)

from apps.rh.models.restriction_medicale import (
    RestrictionMedicale,
)

from apps.rh.serializers.restriction_medicale.restriction_medicale import (
    RestrictionMedicaleSerializer,
    RestrictionMedicaleReadSerializer,
)


class RestrictionMedicaleViewSet(
    BaseViewSet,
):
    """
    API de gestion des restrictions médicales.
    """

    queryset = (
        RestrictionMedicale.objects
        .select_related(
            "evenement",
            "evenement__agent",
        )
        .all()
    )

    serializer_class = (
        RestrictionMedicaleSerializer
    )

    read_serializer_class = (
        RestrictionMedicaleReadSerializer
    )

    search_fields = (

        "evenement__agent__matricule",

        "evenement__agent__nom",

        "evenement__agent__prenom",

    )

    filterset_fields = (

        "date_effet",

        "date_fin",

    )

    ordering = (

        "-date_effet",

        "-created_at",

    )

    select_related_fields = (

        "evenement",

        "evenement__agent",

    )