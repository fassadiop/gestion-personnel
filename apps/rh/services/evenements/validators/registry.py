# apps/rh/services/evenements/validators/registry.py

from .exceptions import ValidationMetierException


class ValidatorRegistry:
    """
    Registre des validators métier.

    Associe un code d'événement à son validator.
    """

    _validators = {}

    @classmethod
    def register(cls, evenement_code, validator_class):
        """
        Enregistre un validator.
        """
        cls._validators[evenement_code] = validator_class

    @classmethod
    def get_validator(cls, evenement):
        """
        Retourne une instance du validator correspondant
        au type d'événement.
        """

        code = evenement.type_evenement.code

        validator_class = cls._validators.get(code)

        if validator_class is None:
            raise ValidationMetierException(
                f"Aucun validator enregistré pour l'événement '{code}'."
            )

        return validator_class()