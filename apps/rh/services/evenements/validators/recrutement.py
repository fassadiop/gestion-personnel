# apps/rh/services/evenements/validators/recrutement.py

from .base import BaseEvenementValidator
from .exceptions import ValidationStatutException


class RecrutementValidator(BaseEvenementValidator):
    """
    Validator de l'événement Recrutement.
    """

    evenement_code = "RECRUTEMENT"

    def validate_specifique(self):
        """
        Vérifie les règles métier propres au recrutement.
        """

        if self.situation is not None:
            raise ValidationStatutException(
                "L'agent possède déjà une situation administrative. "
                "Le recrutement est impossible."
            )