# apps/rh/services/evenements/validators/exceptions.py

class ValidationException(Exception):
    """
    Exception de base du framework de validation métier.
    """
    pass


class ValidationMetierException(ValidationException):
    """
    Violation d'une règle métier.
    """
    pass


class ValidationChronologieException(ValidationException):
    """
    Incohérence dans la chronologie des événements.
    """
    pass


class ValidationReferentielException(ValidationException):
    """
    Incohérence avec un référentiel RH.
    """
    pass


class ValidationOrganisationException(ValidationException):
    """
    Incohérence organisationnelle.
    """
    pass


class ValidationStatutException(ValidationException):
    """
    Statut administratif incompatible.
    """
    pass


class ValidationDocumentException(ValidationException):
    """
    Pièce justificative absente ou invalide.
    """
    pass