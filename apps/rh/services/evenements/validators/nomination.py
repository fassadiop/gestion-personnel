# apps/rh/services/evenements/validators/nomination.py

from .base import BaseEvenementValidator
from .exceptions import (
    ValidationOrganisationException,
    ValidationStatutException,
)


class NominationValidator(BaseEvenementValidator):
    """
    Validator de l'événement Nomination.
    """

    evenement_code = "NOMINATION"

    def validate_specifique(self):
        """
        Vérifie les règles métier propres à la nomination.
        """

        if self.situation is None:
            raise ValidationStatutException(
                "L'agent ne possède aucune situation administrative. "
                "La nomination est impossible."
            )

        if self.evenement.poste is None:
            raise ValidationOrganisationException(
                "Aucun poste n'est renseigné pour cette nomination."
            )