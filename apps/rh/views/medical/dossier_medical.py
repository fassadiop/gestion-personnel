"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/medical/dossier_medical.py

Description :
    ViewSet des dossiers médicaux.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    DossierMedical,
)

from apps.rh.serializers.medical.dossier_medical import (
    DossierMedicalSerializer,
    DossierMedicalReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class DossierMedicalViewSet(
    BaseViewSet
):
    """
    ViewSet des dossiers médicaux.
    """

    queryset = (
        DossierMedical.objects.all()
    )

    serializer_class = (
        DossierMedicalSerializer
    )

    read_serializer_class = (
        DossierMedicalReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "groupe_sanguin",
        "medecin_traitant",
    )

    ordering = (
        "agent__nom",
        "agent__prenom",
    )

    select_related_fields = (
        "agent",
    )