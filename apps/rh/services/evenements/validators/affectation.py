# apps/rh/services/evenements/validators/affectation.py

from .base import BaseEvenementValidator
from .exceptions import (
    ValidationOrganisationException,
    ValidationStatutException,
)


class AffectationValidator(BaseEvenementValidator):
    """
    Validator de l'événement Affectation.
    """

    evenement_code = "AFFECTATION"

    def validate_specifique(self):
        """
        Vérifie les règles métier propres à l'affectation.
        """

        if self.situation is None:
            raise ValidationStatutException(
                "L'agent ne possède aucune situation administrative. "
                "L'affectation est impossible."
            )

        if self.evenement.unite_organisationnelle is None:
            raise ValidationOrganisationException(
                "L'unité organisationnelle est obligatoire."
            )