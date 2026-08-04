"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/views/profil_administration.py

Description :
    ViewSet de gestion des profils d'administration.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.administration.views.base import BaseAdministrationViewSet

from apps.administration.models.profil_administration import (
    ProfilAdministration,
)

from apps.administration.serializers.profil_administration import (
    ProfilAdministrationSerializer,
    ProfilAdministrationReadSerializer,
)


class ProfilAdministrationViewSet(BaseAdministrationViewSet):
    """
    Gestion des profils d'administration.
    """

    queryset = (
        ProfilAdministration.objects
        .select_related(
            "user",
            "structure_racine",
        )
        .all()
    )

    serializer_class = (
        ProfilAdministrationSerializer
    )

    read_serializer_class = (
        ProfilAdministrationReadSerializer
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "structure_racine__code",
        "structure_racine__libelle",
    )

    ordering_fields = (
        "user__username",
        "structure_racine__libelle",
    )

    filterset_fields = (
        "structure_racine",
        "actif",
    )