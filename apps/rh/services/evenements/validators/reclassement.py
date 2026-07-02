# apps/rh/services/evenements/validators/reclassement.py

from .base import BaseEvenementValidator
from .exceptions import (
    ValidationReferentielException,
    ValidationStatutException,
)


class ReclassementValidator(BaseEvenementValidator):
    """
    Validator de l'événement Reclassement.
    """

    evenement_code = "RECLASSEMENT"

    def validate_specifique(self):
        """
        Vérifie les règles métier propres au reclassement.
        """

        if self.situation is None:
            raise ValidationStatutException(
                "L'agent ne possède aucune situation administrative. "
                "Le reclassement est impossible."
            )

        if self.evenement.corps is None:
            raise ValidationReferentielException(
                "Le corps est obligatoire."
            )

        if self.evenement.grade is None:
            raise ValidationReferentielException(
                "Le grade est obligatoire."
            )

        if self.evenement.classe is None:
            raise ValidationReferentielException(
                "La classe est obligatoire."
            )

        if self.evenement.echelon is None:
            raise ValidationReferentielException(
                "L'échelon est obligatoire."
            )