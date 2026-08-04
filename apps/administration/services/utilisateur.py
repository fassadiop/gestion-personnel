"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/services/utilisateur.py

Description :
    Services de gestion des utilisateurs.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import transaction
from django.utils.crypto import get_random_string

import re
import unicodedata

from rest_framework.exceptions import ValidationError

from apps.administration.models.profil_administration import (
    ProfilAdministration,
)
from apps.rh.models.agent import Agent

User = get_user_model()


class UtilisateurService:
    """
    Service métier de gestion
    des utilisateurs du SGCP.
    """

    @classmethod
    @transaction.atomic
    def creer_utilisateur(
        cls,
        *,
        agent: Agent,
        groupes=None,
    ):
        """
        Crée un compte utilisateur
        pour un agent.
        """

        if agent.user is not None:
            raise ValidationError(
                {
                    "agent": (
                        "Cet agent possède déjà un compte utilisateur."
                    )
                }
            )

        username = cls._generer_username(
            agent.prenom,
            agent.nom,
        )

        if (
            agent.email
            and User.objects.filter(
                email=agent.email
            ).exists()
        ):
            raise ValidationError(
                {
                    "email": (
                        "Cette adresse e-mail est déjà utilisée."
                    )
                }
            )

        mot_de_passe = get_random_string(12)

        user = User.objects.create_user(
            username=username,
            email=agent.email,
            first_name=agent.prenom,
            last_name=agent.nom,
            password=mot_de_passe,
            is_active=agent.actif,
        )

        # Liaison Agent → User
        agent.user = user

        agent.save(
            update_fields=[
                "user",
            ]
        )

        cls._creer_profil_administration(
            user=user,
            agent=agent,
        )

        if groupes:
            user.groups.set(groupes)

        return {
            "user": user,
            "username": username,
            "password": mot_de_passe,
        }

    @staticmethod
    def _generer_username(
        prenom: str,
        nom: str,
    ) -> str:
        """
        Génère automatiquement un nom
        d'utilisateur unique selon la règle :

            premier_prenom.nom

        Les accents et caractères spéciaux
        sont supprimés.
        """

        def normaliser(texte: str) -> str:
            texte = unicodedata.normalize(
                "NFKD",
                texte,
            ).encode(
                "ascii",
                "ignore",
            ).decode(
                "ascii",
            )

            texte = texte.lower()

            texte = re.sub(
                r"[^a-z0-9\s]",
                "",
                texte,
            )

            texte = ".".join(
                texte.split()
            )

            return texte

        premier_prenom = (
            prenom.strip().split()[0]
        )

        base = (
            f"{normaliser(premier_prenom)}."
            f"{normaliser(nom)}"
        )

        username = base

        compteur = 1

        while User.objects.filter(
            username=username,
        ).exists():

            username = (
                f"{base}{compteur}"
            )

            compteur += 1

        return username

    @staticmethod
    def _creer_profil_administration(
        *,
        user,
        agent,
    ):
        """
        Crée le profil d'administration
        associé à un utilisateur.
        """

        ProfilAdministration.objects.create(
            user=user,
            structure_racine=agent.structure_racine,
        )

    @classmethod
    @transaction.atomic
    def reinitialiser_mot_de_passe(
        cls,
        *,
        user,
    ):
        """
        Réinitialise le mot de passe
        d'un utilisateur.
        """

        mot_de_passe = get_random_string(12)

        user.set_password(
            mot_de_passe,
        )

        user.save(
            update_fields=[
                "password",
            ],
        )

        return {
            "user": user,
            "password": mot_de_passe,
        }

    @classmethod
    @transaction.atomic
    def changer_statut(
        cls,
        *,
        user,
    ):
        """
        Active ou désactive
        un compte utilisateur.
        """

        user.is_active = not user.is_active

        user.save(
            update_fields=[
                "is_active",
            ],
        )

        return user