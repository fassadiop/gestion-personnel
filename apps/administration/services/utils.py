"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/services/utils.py

Description :
    Fonctions utilitaires du module Administration.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User = get_user_model()


def generer_mot_de_passe(
    longueur: int = 12,
) -> str:
    """
    Génère un mot de passe temporaire.
    """

    return get_random_string(longueur)


def username_existe(
    username: str,
) -> bool:
    """
    Vérifie si un nom d'utilisateur
    existe déjà.
    """

    return User.objects.filter(
        username=username,
    ).exists()


def generer_username(
    nom: str,
    prenom: str,
) -> str:
    """
    Génère automatiquement un nom
    d'utilisateur unique.

    Format :

        pnom
        pnom1
        pnom2
        ...
    """

    username = (
        f"{prenom[:1]}{nom}"
        .lower()
        .replace(" ", "")
    )

    candidat = username

    index = 1

    while username_existe(
        candidat,
    ):
        candidat = (
            f"{username}{index}"
        )

        index += 1

    return candidat