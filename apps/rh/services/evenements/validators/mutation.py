# apps/rh/services/evenements/validators/mutation.py

from .base import BaseEvenementValidator
from .exceptions import (
    ValidationOrganisationException,
    ValidationStatutException,
)


class MutationValidator(BaseEvenementValidator):
    """
    Validator de l'événement Mutation.
    """

    evenement_code = "MUTATION"

    def validate_specifique(self):
        """
        Vérifie les règles métier propres à la mutation.
        """

        if self.situation is None:
            raise ValidationStatutException(
                "L'agent ne possède aucune situation administrative. "
                "La mutation est impossible."
            )

        if self.affectation is None:
            raise ValidationOrganisationException(
                "L'agent ne possède aucune affectation en cours."
            )

        if self.evenement.unite_organisationnelle is None:
            raise ValidationOrganisationException(
                "L'unité organisationnelle de destination est obligatoire."
            )