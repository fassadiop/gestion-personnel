# apps/rh/services/evenements/validation.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/validation.py

Description :
    Orchestrateur principal du moteur de carrière.

    Cette classe constitue le point d'entrée unique
    de l'exécution des événements de carrière.

Auteur : SGCP
Version : 2.3
==========================================================
"""

from django.db import transaction

# Chargement automatique des handlers afin
# d'alimenter le HandlerRegistry.
from apps.rh.services.evenements import handlers  # noqa: F401

from apps.rh.services.evenements.context import (
    ExecutionContext,
)

from apps.rh.services.evenements.exceptions import (
    EvenementInvalideError,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)


class ValidationEvenementService:
    """
    Orchestrateur du moteur de carrière.

    Responsabilités :

        • Vérifier les paramètres d'entrée.
        • Construire le contexte d'exécution.
        • Résoudre le handler adapté.
        • Ouvrir une transaction.
        • Exécuter le handler.
        • Déclencher les hooks techniques.

    Aucune règle métier ne doit être
    implémentée ici.
    """

    @transaction.atomic
    def executer(
        self,
        *,
        evenement,
        utilisateur=None,
        request=None,
    ):
        """
        Exécute un événement de carrière.
        """

        self._validate_input(
            evenement,
        )

        context = ExecutionContext(

            evenement=evenement,

            utilisateur=utilisateur,

            request=request,

        )

        handler = self._get_handler(
            context,
        )

        self._before_execute(
            context,
            handler,
        )

        result = handler.execute()

        self._after_execute(
            context,
            handler,
            result,
        )

        return result

    # =====================================================
    # Résolution du handler
    # =====================================================

    def _get_handler(
        self,
        context,
    ):
        """
        Retourne le handler correspondant.
        """

        return HandlerRegistry.get_handler(
            context,
        )

    # =====================================================
    # Validation technique
    # =====================================================

    def _validate_input(
        self,
        evenement,
    ):
        """
        Vérifie les paramètres d'entrée.
        """

        if evenement is None:
            raise EvenementInvalideError(
                "Aucun événement fourni."
            )

        if evenement.pk is None:
            raise EvenementInvalideError(
                "L'événement doit être enregistré "
                "avant son exécution."
            )

        if evenement.agent is None:
            raise EvenementInvalideError(
                "Aucun agent associé à l'événement."
            )

        if evenement.type_evenement is None:
            raise EvenementInvalideError(
                "Le type d'événement est obligatoire."
            )

        if evenement.date_effet is None:
            raise EvenementInvalideError(
                "La date d'effet est obligatoire."
            )

        if not evenement.actif:
            raise EvenementInvalideError(
                "L'événement est inactif."
            )

    # =====================================================
    # Hooks
    # =====================================================

    def _before_execute(
        self,
        context,
        handler,
    ):
        """
        Hook exécuté avant le traitement.

        Réservé aux futures évolutions :

            • Audit
            • Journalisation
            • Workflow
            • Sécurité
        """
        pass

    def _after_execute(
        self,
        context,
        handler,
        result,
    ):
        """
        Hook exécuté après le traitement.

        Réservé aux futures évolutions :

            • Notifications
            • Bus d'événements
            • Statistiques
            • Signature électronique
        """
        pass