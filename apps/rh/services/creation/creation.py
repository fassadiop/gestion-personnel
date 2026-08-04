"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creation.py

Description :
    Service de création des événements
    de carrière.

Auteur : SGCP
Version : 2.1
==========================================================
"""

from django.db import transaction
from apps.rh.services.creation import creators
from apps.rh.services.creation.context import (
    CreationContext,
)

from apps.rh.services.creation.registry import (
    CreationRegistry,
)


class EvenementCreationService:
    """
    Orchestre la création d'un événement
    de carrière.

    Responsabilités :

        - construire le contexte ;

        - identifier le Creator ;

        - ouvrir une transaction ;

        - déléguer la création.

    Il ne contient aucune règle métier.
    """

    @transaction.atomic
    def creer(
        self,
        *,
        validated_data,
        payload,
        utilisateur=None,
        request=None,
    ):
        """
        Crée un événement complet.
        """

        context = CreationContext(

            validated_data=validated_data,

            payload=payload,

            utilisateur=utilisateur,

            request=request,

        )

        creator_class = (
            self._get_creator(context)
        )

        creator = creator_class(
            context=context,
        )

        return creator.create()

    # =====================================================
    # Méthodes privées
    # =====================================================

    def _get_creator(
        self,
        context,
    ):
        """
        Retourne le Creator correspondant
        au type d'événement.
        """

        code_evenement = (
            context.validated_data[
                "type_evenement"
            ].code
        )

        return CreationRegistry.get_creator(
            code_evenement
        )