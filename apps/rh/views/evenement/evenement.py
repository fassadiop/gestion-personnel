"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/evenement/evenement.py

Description :
    ViewSet des événements de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.rh.models.evenement import (
    EvenementCarriere,
)

from apps.rh.serializers.evenement.evenement_detail import (
    EvenementCarriereDetailSerializer,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereSerializer,
    EvenementCarriereReadSerializer,
)

from apps.rh.services.evenements.validation import (
    ValidationEvenementService,
)

from apps.rh.views.base import BaseViewSet


class EvenementCarriereViewSet(
    BaseViewSet
):
    """
    ViewSet des événements de carrière.
    """

    queryset = (
        EvenementCarriere.objects.all()
    )

    serializer_class = (
        EvenementCarriereSerializer
    )

    read_serializer_class = (
        EvenementCarriereReadSerializer
    )

    detail_serializer_class = (
        EvenementCarriereDetailSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "type_evenement__libelle",
        "reference_acte",
        "objet",
    )

    ordering = (
        "-created_at",
    )

    select_related_fields = (
        "agent",
        "type_evenement",
        "position_administrative",
    )

    def get_serializer_class(self):
        """
        Retourne le serializer selon l'action.
        """

        if self.action == "retrieve":
            return EvenementCarriereDetailSerializer

        if self.action == "list":
            return self.read_serializer_class

        return self.serializer_class

    @action(
        detail=True,
        methods=["post"],
        url_path="valider",
    )
    def valider(self, request, pk=None):
        """
        Valide un événement de carrière.
        """

        evenement = self.get_object()

        service = ValidationEvenementService()

        service.executer(
            evenement=evenement,
            utilisateur=request.user,
            request=request,
        )

        return Response(
            {
                "detail": (
                    "Événement de carrière validé avec succès."
                )
            },
            status=status.HTTP_200_OK,
        )