"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/services/creation_compte.py

Description :
    Service métier de création d'un compte utilisateur.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.exceptions import ValidationError

from apps.administration.models.profil_administration import (
    ProfilAdministration,
)
from apps.administration.services.utils import (
    generer_mot_de_passe,
    generer_username,
)
from apps.rh.models.agent import Agent

User = get_user_model()


class CreationCompteService:
    """
    Service métier chargé de créer
    un compte utilisateur.
    """

    @classmethod
    @transaction.atomic
    def executer(
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

        username = generer_username(
            nom=agent.nom,
            prenom=agent.prenom,
        )

        mot_de_passe = generer_mot_de_passe()

        user = User.objects.create_user(
            username=username,
            email=agent.email,
            first_name=agent.prenom,
            last_name=agent.nom,
            password=mot_de_passe,
            is_active=agent.actif,
        )

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
    def _creer_profil_administration(
        *,
        user,
        agent,
    ):
        """
        Crée le profil d'administration.
        """

        ProfilAdministration.objects.create(
            user=user,
            structure_racine=agent.structure_racine,
        )