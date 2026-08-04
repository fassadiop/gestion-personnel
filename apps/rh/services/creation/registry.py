"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/registry.py

Description :
    Registre des Creators du moteur de création
    des événements de carrière.

Auteur : SGCP
Version : 1.1
==========================================================
"""

from apps.rh.services.creation.base import (
    BaseEvenementCreator,
)

from apps.rh.services.creation.exceptions import (
    CreatorIntrouvableError,
)


class CreationRegistry:
    """
    Registre des Creators.

    Associe un code de type d'événement
    à son Creator spécialisé.
    """

    _creators = {}

    @classmethod
    def register(
        cls,
        code_evenement,
        creator_class,
    ):
        """
        Enregistre un Creator.
        """

        code = code_evenement.upper()

        if code in cls._creators:
            raise ValueError(
                f"Le Creator '{code}' "
                "est déjà enregistré."
            )

        if not issubclass(
            creator_class,
            BaseEvenementCreator,
        ):
            raise TypeError(
                "Le Creator doit hériter de "
                "BaseEvenementCreator."
            )

        cls._creators[code] = creator_class

    @classmethod
    def get_creator(
        cls,
        code_evenement,
    ):
        """
        Retourne le Creator correspondant.
        """

        code = code_evenement.upper()

        creator = cls._creators.get(code)

        if creator is None:
            raise CreatorIntrouvableError(
                f"Aucun Creator enregistré "
                f"pour '{code}'."
            )

        return creator

    @classmethod
    def list_creators(cls):
        """
        Retourne les Creators enregistrés.
        """

        return dict(cls._creators)

    @classmethod
    def clear(cls):
        """
        Vide le registre.

        Utilisé uniquement
        pour les tests unitaires.
        """

        cls._creators.clear()