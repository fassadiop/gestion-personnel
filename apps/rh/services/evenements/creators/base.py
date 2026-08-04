"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/creators/base.py

Description :
    Classe de base de tous les créateurs
    d'événements de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from abc import ABC, abstractmethod

from django.db import transaction

from apps.rh.models.evenement import EvenementCarriere


class BaseCreator(ABC):
    """
    Classe de base des créateurs d'événements.

    Un Creator prépare exclusivement la fiche
    spécialisée d'un événement de carrière.

    Il ne modifie jamais la carrière de l'agent.

    Toute la logique métier est exécutée
    ultérieurement par le Handler.
    """

    def __init__(self, evenement: EvenementCarriere):
        self.evenement = evenement
        self.agent = evenement.agent
        self.structure = evenement.structure

    @transaction.atomic
    def execute(self):
        """
        Point d'entrée unique du Creator.
        """

        self.before_execute()

        self.validate()

        result = self.process()

        self.after_execute()

        return result

    def before_execute(self):
        """
        Hook exécuté avant le traitement.

        Peut être surchargé si nécessaire.
        """
        pass

    def validate(self):
        """
        Validation technique.

        Peut être surchargée par les
        classes filles.
        """
        pass

    @abstractmethod
    def process(self):
        """
        Crée la fiche spécialisée.

        Doit être implémentée dans chaque
        Creator.
        """
        raise NotImplementedError

    def after_execute(self):
        """
        Hook exécuté après le traitement.

        Peut être surchargé si nécessaire.
        """
        pass