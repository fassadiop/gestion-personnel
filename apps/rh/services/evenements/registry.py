"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/registry.py

Description :
    Registre officiel des handlers du moteur
    de carrière.

Auteur : SGCP
Version : 2.2
==========================================================
"""

from typing import Dict, Type

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.context import (
    ExecutionContext,
)

from apps.rh.services.evenements.exceptions import (
    HandlerAlreadyRegisteredError,
    HandlerNotFoundError,
)


class HandlerRegistry:
    """
    Registre central des handlers du moteur
    de carrière.

    Associe chaque type d'événement
    à son handler.
    """

    _handlers: Dict[
        str,
        Type[BaseEvenementHandler],
    ] = {}

    # =====================================================
    # Enregistrement
    # =====================================================

    @classmethod
    def register(
        cls,
        code_evenement: str,
        handler_class: Type[BaseEvenementHandler],
    ):
        """
        Enregistre un handler.
        """

        if not code_evenement:
            raise ValueError(
                "Le code de l'événement est obligatoire."
            )

        code = code_evenement.upper()

        if code in cls._handlers:
            raise HandlerAlreadyRegisteredError(
                f"Le handler '{code}' est déjà enregistré."
            )

        if not issubclass(
            handler_class,
            BaseEvenementHandler,
        ):
            raise TypeError(
                f"{handler_class.__name__} "
                "doit hériter de "
                "BaseEvenementHandler."
            )

        cls._handlers[code] = handler_class

        return handler_class

    # =====================================================
    # Résolution
    # =====================================================

    @classmethod
    def get_handler(
        cls,
        context: ExecutionContext,
    ) -> BaseEvenementHandler:
        """
        Retourne une instance du handler
        correspondant au contexte
        d'exécution.
        """

        if context is None:
            raise HandlerNotFoundError(
                "Aucun contexte fourni."
            )

        evenement = context.evenement

        if evenement is None:
            raise HandlerNotFoundError(
                "Aucun événement fourni."
            )

        if evenement.type_evenement is None:
            raise HandlerNotFoundError(
                "Le type d'événement est obligatoire."
            )

        code = (
            evenement.type_evenement.code.upper()
        )

        handler_class = cls._handlers.get(
            code
        )

        if handler_class is None:
            raise HandlerNotFoundError(
                "Aucun handler enregistré pour "
                f"le type d'événement '{code}'."
            )

        return handler_class(
            context=context,
        )

    # =====================================================
    # Utilitaires
    # =====================================================

    @classmethod
    def has_handler(
        cls,
        code_evenement: str,
    ) -> bool:
        """
        Vérifie qu'un handler est enregistré.
        """

        if not code_evenement:
            return False

        return (
            code_evenement.upper()
            in cls._handlers
        )

    @classmethod
    def unregister(
        cls,
        code_evenement: str,
    ):
        """
        Supprime un handler.

        Principalement utilisé pour les tests.
        """

        if not code_evenement:
            return

        cls._handlers.pop(
            code_evenement.upper(),
            None,
        )

    @classmethod
    def clear(cls):
        """
        Vide complètement le registre.

        Principalement utilisé pour les tests.
        """

        cls._handlers.clear()

    @classmethod
    def get_registered_handlers(
        cls,
    ) -> Dict[
        str,
        Type[BaseEvenementHandler],
    ]:
        """
        Retourne tous les handlers enregistrés.
        """

        return cls._handlers.copy()