"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : authentication/views.py

Description :
    Vues d'authentification.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.serializers import (
    LoginSerializer,
    RefreshTokenSerializer,
)
from apps.authentication.services import (
    AuthenticationService,
)

from apps.authentication.serializers import (
    CurrentUserSerializer,
)


class LoginView(APIView):
    """
    Authentifie un utilisateur.
    """

    permission_classes = ()

    def post(
        self,
        request,
    ):
        serializer = LoginSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        data = AuthenticationService.login(
            serializer.validated_data["user"],
        )

        return Response(
            data,
            status=status.HTTP_200_OK,
        )


class RefreshTokenView(APIView):
    """
    Génère un nouveau token d'accès.
    """

    permission_classes = ()

    def post(
        self,
        request,
    ):
        serializer = RefreshTokenSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        data = AuthenticationService.refresh(
            serializer.validated_data["refresh"],
        )

        return Response(
            data,
            status=status.HTTP_200_OK,
        )


class LogoutView(APIView):
    """
    Déconnecte un utilisateur.
    """

    permission_classes = (
        IsAuthenticated,
    )

    def post(
        self,
        request,
    ):
        serializer = RefreshTokenSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        AuthenticationService.logout(
            serializer.validated_data["refresh"],
        )

        return Response(
            {
                "detail": (
                    "Déconnexion effectuée avec succès."
                )
            },
            status=status.HTTP_200_OK,
        )


class CurrentUserView(APIView):
    """
    Retourne l'utilisateur connecté.
    """

    permission_classes = (
        IsAuthenticated,
    )

    def get(
        self,
        request,
    ):
        serializer = CurrentUserSerializer(
            request.user,
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )