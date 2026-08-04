# apps/rh/views/inaptitude_medicale/inaptitude_medicale.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/inaptitude_medicale/inaptitude_medicale.py

Description :
    ViewSet des inaptitudes médicales.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.views.base import (
    BaseViewSet,
)

from apps.rh.models.inaptitude_medicale import (
    InaptitudeMedicale,
)

from apps.rh.serializers.inaptitude_medicale.inaptitude_medicale import (
    InaptitudeMedicaleSerializer,
    InaptitudeMedicaleReadSerializer,
)


class InaptitudeMedicaleViewSet(
    BaseViewSet,
):
    """
    API de gestion des inaptitudes médicales.
    """

    queryset = (
        InaptitudeMedicale.objects
        .select_related(
            "evenement",
            "evenement__agent",
            "type_inaptitude",
        )
        .all()
    )

    serializer_class = (
        InaptitudeMedicaleSerializer
    )

    read_serializer_class = (
        InaptitudeMedicaleReadSerializer
    )

    search_fields = (

        "evenement__agent__matricule",

        "evenement__agent__nom",

        "evenement__agent__prenom",

    )

    filterset_fields = (

        "type_inaptitude",

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

        "type_inaptitude",

    )