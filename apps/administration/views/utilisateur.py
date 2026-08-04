"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/views/utilisateur.py

Description :
    ViewSet de gestion des utilisateurs.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.administration.views.base import (
    BaseAdministrationViewSet,
)

from apps.administration.serializers.utilisateur import (
    UtilisateurSerializer,
    UtilisateurReadSerializer,
)

from apps.administration.serializers.utilisateur_create import (
    UtilisateurCreateSerializer,
)

from apps.administration.services.utilisateur import (
    UtilisateurService,
)

User = get_user_model()


class UtilisateurViewSet(BaseAdministrationViewSet):
    """
    Gestion des comptes utilisateurs du SGCP.
    """

    queryset = (
        User.objects
        .select_related(
            "agent",
            "profil_administration",
        )
        .prefetch_related(
            "groups",
        )
    )

    serializer_class = UtilisateurSerializer

    read_serializer_class = (
        UtilisateurReadSerializer
    )

    detail_serializer_class = (
        UtilisateurReadSerializer
    )

    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )

    ordering_fields = (
        "username",
        "last_name",
        "date_joined",
    )

    filterset_fields = (
        "is_active",
        "is_superuser",
    )

    def get_serializer_class(self):
        """
        Sélectionne automatiquement
        le serializer selon l'action.
        """

        if self.action == "create":
            return UtilisateurCreateSerializer

        return super().get_serializer_class()

    def create(
        self,
        request,
        *args,
        **kwargs,
    ):
        """
        Création d'un compte utilisateur
        à partir d'un agent.
        """

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        validated = serializer.validated_data

        resultat = (
            UtilisateurService.creer_utilisateur(
                agent=validated["agent"],
                groupes=validated.get(
                    "groupes",
                    [],
                ),
            )
        )

        output = self.get_read_serializer(
            resultat["user"],
        )

        return Response(
            {
                **output.data,
                "password": resultat["password"],
            },
            status=status.HTTP_201_CREATED,
        )

    @action(
        detail=True,
        methods=["post"],
        url_path="reinitialiser-mot-de-passe",
    )
    def reinitialiser_mot_de_passe(
        self,
        request,
        pk=None,
    ):
        """
        Réinitialise le mot de passe
        d'un utilisateur.
        """

        user = self.get_object()

        resultat = (
            UtilisateurService.reinitialiser_mot_de_passe(
                user=user,
            )
        )

        return Response(
            {
                "message": (
                    "Mot de passe réinitialisé avec succès."
                ),
                "password": resultat["password"],
            },
            status=status.HTTP_200_OK,
        )

    @action(
        detail=True,
        methods=["post"],
        url_path="changer-statut",
    )
    def changer_statut(
        self,
        request,
        pk=None,
    ):
        """
        Active ou désactive
        un compte utilisateur.
        """

        user = self.get_object()

        UtilisateurService.changer_statut(
            user=user,
        )

        serializer = self.get_read_serializer(
            user,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    