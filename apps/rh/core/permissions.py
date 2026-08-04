"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : core/permissions.py

Description :
    Permissions communes du SGCP.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework.permissions import BasePermission


class IsAuthenticatedAndActive(BasePermission):
    """
    Autorise uniquement les utilisateurs
    authentifiés et actifs.
    """

    def has_permission(
        self,
        request,
        view,
    ):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_active
        )