"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : authentication/services.py

Description :
    Services d'authentification.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework_simplejwt.tokens import (
    RefreshToken,
)


class AuthenticationService:
    """
    Service d'authentification.

    Centralise toute la logique liée
    à l'authentification des utilisateurs.
    """

    @staticmethod
    def login(
        user,
    ):
        """
        Génère les tokens JWT d'un utilisateur.
        """

        refresh = RefreshToken.for_user(
            user
        )

        return {
            "access": str(
                refresh.access_token
            ),
            "refresh": str(
                refresh
            ),
        }

    @staticmethod
    def refresh(
        refresh_token,
    ):
        """
        Génère un nouveau token d'accès
        à partir d'un refresh token.
        """

        refresh = RefreshToken(
            refresh_token
        )

        return {
            "access": str(
                refresh.access_token
            ),
        }

    @staticmethod
    def logout(
        refresh_token,
    ):
        """
        Invalide un refresh token.
        """

        token = RefreshToken(
            refresh_token
        )

        token.blacklist()