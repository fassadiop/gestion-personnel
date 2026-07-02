"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/registry.py

Description :
    Registre officiel des handlers du moteur
    de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.services.evenements.base import BaseEvenementHandler
from apps.rh.services.evenements.exceptions import (
    HandlerAlreadyRegisteredError,
    HandlerNotFoundError,
)


class HandlerRegistry:
    """
    Registre central des handlers du moteur de carrière.

    Associe un code de type d'événement à la classe
    responsable de son traitement.

    Ce registre constitue le point d'entrée unique
    permettant de résoudre le handler adapté à un
    événement de carrière.

    Exemple
    --------
        HandlerRegistry.register(
            "PROMOTION",
            PromotionHandler,
        )

        handler = HandlerRegistry.get_handler(
            evenement
        )

        handler.execute()
    """

    _handlers = {}

    # =====================================================
    # Enregistrement
    # =====================================================

    @classmethod
    def register(cls, code_evenement, handler_class):
        """
        Enregistre un handler.

        Args:
            code_evenement (str):
                Code métier du type d'événement.

            handler_class (type):
                Classe héritant de BaseEvenementHandler.
        """

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

    # =====================================================
    # Recherche
    # =====================================================

    @classmethod
    def get_handler(cls, evenement):
        """
        Retourne une instance du handler adapté.

        Args:
            evenement:
                Instance de EvenementCarriere.

        Returns:
            BaseEvenementHandler
        """

        code = evenement.type_evenement.code.upper()

        handler_class = cls._handlers.get(code)

        if handler_class is None:
            raise HandlerNotFoundError(
                "Aucun handler enregistré pour "
                f"le type d'événement '{code}'."
            )

        return handler_class(evenement)

    # =====================================================
    # Utilitaires
    # =====================================================

    @classmethod
    def has_handler(cls, code_evenement):
        """
        Vérifie qu'un handler est enregistré.
        """

        return (
            code_evenement.upper()
            in cls._handlers
        )

    @classmethod
    def unregister(cls, code_evenement):
        """
        Supprime un handler.

        Principalement utilisé pour les tests.
        """

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
    def registered_handlers(cls):
        """
        Retourne la liste des handlers enregistrés.

        Returns:
            dict
        """

        return cls._handlers.copy()