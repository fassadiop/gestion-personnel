# apps/rh/services/evenements/exceptions.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/exceptions.py

Description :
    Exceptions métier du moteur de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""


class EvenementError(Exception):
    """
    Exception de base du moteur de carrière.
    """

    pass


class EvenementInvalideError(EvenementError):
    """
    L'événement ne respecte pas les règles métier.
    """

    pass


class EvenementDejaValideError(EvenementError):
    """
    L'événement est déjà validé.
    """

    pass


class StatutEvenementInvalideError(EvenementError):
    """
    Le statut de l'événement ne permet pas son exécution.
    """

    pass


class HandlerIntrouvableError(EvenementError):
    """
    Aucun handler n'est enregistré pour ce type d'événement.
    """

    pass


class SituationAdministrativeError(EvenementError):
    """
    Erreur liée à la situation administrative.
    """

    pass


class AffectationError(EvenementError):
    """
    Erreur liée aux affectations.
    """

    pass


class OccupationPosteError(EvenementError):
    """
    Erreur liée à l'occupation des postes.
    """

    pass


class DocumentAdministratifError(EvenementError):
    """
    Erreur liée aux documents administratifs.
    """

    pass


class HandlerAlreadyRegisteredError(EvenementError):
    """
    Levée lorsqu'un handler est enregistré
    plusieurs fois.
    """
    pass


class HandlerNotFoundError(EvenementError):
    """
    Levée lorsqu'aucun handler n'existe
    pour un type d'événement.
    """
    pass