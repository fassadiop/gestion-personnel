# apps/rh/services/evenements/validators/base.py

from abc import ABC, abstractmethod

from services.evenements.utils import load_evenement_data
from .exceptions import (
    ValidationException,
    ValidationMetierException,
)


class BaseEvenementValidator(ABC):
    """
    Classe de base de tous les validators métier.

    Un validator ne modifie jamais les données.
    Il vérifie uniquement qu'un événement respecte
    les règles métier avant son traitement.
    """

    evenement_code = None

    def __init__(self):
        self.evenement = None
        self.data = {}

        self.agent = None
        self.situation = None
        self.affectation = None
        self.occupation = None

    def initialise(self, evenement):
        """
        Charge le contexte de validation.
        """

        self.evenement = evenement
        self.data = load_evenement_data(evenement)

        self.agent = self.data.get("agent")
        self.situation = self.data.get("situation")
        self.affectation = self.data.get("affectation")
        self.occupation = self.data.get("occupation")

    def validate(self, evenement):
        """
        Point d'entrée unique du validator.
        """

        self.initialise(evenement)

        self.validate_agent()

        self.validate_date()

        self.validate_specifique()

    def validate_agent(self):
        """
        Vérifie que l'agent existe.
        """

        if self.agent is None:
            raise ValidationMetierException(
                "Aucun agent associé à cet événement."
            )

    def validate_date(self):
        """
        Vérifie que la date d'effet est renseignée.
        """

        if self.evenement.date_effet is None:
            raise ValidationException(
                "La date d'effet est obligatoire."
            )

    @abstractmethod
    def validate_specifique(self):
        """
        Validation propre à chaque événement.
        """
        pass