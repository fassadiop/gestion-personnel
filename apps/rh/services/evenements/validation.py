# apps/rh/services/evenements/validation.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/validation.py

Description :
    Orchestrateur principal du moteur de carrière.

    Cette classe constitue le point d'entrée unique
    de l'exécution des événements de carrière.

    Responsabilités :
        - Vérifier les paramètres d'entrée.
        - Résoudre le validator approprié.
        - Exécuter les validations métier.
        - Résoudre le handler approprié.
        - Encadrer le traitement dans une transaction.
        - Retourner le résultat du traitement.

Auteur : SGCP
Version : 1.1
==========================================================
"""

# ==========================================================
# Chargement automatique des registres
# ==========================================================

# Force le chargement des handlers afin
# d'alimenter automatiquement le HandlerRegistry.
from apps.rh.services.evenements import handlers  # noqa: F401

# Force le chargement des validators afin
# d'alimenter automatiquement le ValidatorRegistry.
from apps.rh.services.evenements import validators  # noqa: F401

# ==========================================================
# Imports
# ==========================================================

from django.db import transaction

from apps.rh.services.evenements.exceptions import (
    EvenementInvalideError,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.validators.registry import (
    ValidatorRegistry,
)


class ValidationEvenementService:
    """
    Orchestrateur principal du moteur de carrière.

    Cette classe ne contient aucune règle métier.

    Elle coordonne simplement les différentes
    étapes du traitement d'un événement.
    """

    def executer(self, evenement):
        """
        Valide puis exécute un événement de carrière.

        Étapes :
            1. Vérification des paramètres.
            2. Résolution du validator.
            3. Validation métier.
            4. Résolution du handler.
            5. Exécution du traitement.
            6. Retour du résultat.

        Args:
            evenement:
                Instance de EvenementCarriere.

        Returns:
            Résultat retourné par le handler.
        """

        # ==================================================
        # Vérification des paramètres
        # ==================================================

        if evenement is None:
            raise EvenementInvalideError(
                "Aucun événement fourni."
            )

        # ==================================================
        # Résolution du validator
        # ==================================================

        validator = ValidatorRegistry.get_validator(
            evenement
        )

        # ==================================================
        # Validation métier
        # ==================================================

        validator.validate(evenement)

        # ==================================================
        # Résolution du handler
        # ==================================================

        handler = HandlerRegistry.get_handler(
            evenement
        )

        # ==================================================
        # Hook avant traitement
        # ==================================================

        self._before_execute(evenement)

        # ==================================================
        # Traitement transactionnel
        # ==================================================

        with transaction.atomic():

            result = handler.execute()

        # ==================================================
        # Hook après traitement
        # ==================================================

        self._after_execute(
            evenement,
            result,
        )

        return result

    # ======================================================
    # Hooks
    # ======================================================

    def _before_execute(self, evenement):
        """
        Hook exécuté avant le traitement.

        Réservé aux évolutions futures :
            - journalisation
            - workflow
            - contrôles complémentaires
        """
        pass

    def _after_execute(self, evenement, result):
        """
        Hook exécuté après le traitement.

        Réservé aux évolutions futures :
            - audit
            - notifications
            - statistiques
            - bus d'événements
        """
        pass