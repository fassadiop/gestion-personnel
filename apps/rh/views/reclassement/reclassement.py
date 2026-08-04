"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/carriere/reclassement.py

Description :
    ViewSet des reclassements.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models import Reclassement

from apps.rh.serializers.reclassement.reclassement import (
    ReclassementSerializer,
    ReclassementReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class ReclassementViewSet(BaseViewSet):
    """
    ViewSet des reclassements.
    """

    queryset = Reclassement.objects.all()

    serializer_class = ReclassementSerializer

    read_serializer_class = ReclassementReadSerializer

    search_fields = (
        "evenement__agent__matricule",
        "evenement__agent__nom",
        "evenement__agent__prenom",
        "corps__libelle",
        "grade__libelle",
        "classe__libelle",
        "echelon__libelle",
        "evenement__reference_acte",
        "evenement__objet",
    )

    ordering = (
        "-evenement__date_effet",
        "-created_at",
    )

    select_related_fields = (
        "evenement",
        "evenement__agent",
        "corps",
        "grade",
        "classe",
        "echelon",
    )