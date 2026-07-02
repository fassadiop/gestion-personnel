# apps/rh/services/evenements/validators/titularisation.py

from .base import BaseEvenementValidator
from .exceptions import ValidationStatutException


class TitularisationValidator(BaseEvenementValidator):
    """
    Validator de l'événement Titularisation.
    """

    evenement_code = "TITULARISATION"

    def validate_specifique(self):
        """
        Vérifie les règles métier propres à la titularisation.
        """

        if self.situation is None:
            raise ValidationStatutException(
                "L'agent ne possède aucune situation administrative. "
                "La titularisation est impossible."
            )