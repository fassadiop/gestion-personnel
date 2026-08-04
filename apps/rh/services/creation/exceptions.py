"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/exceptions.py

Description :
    Exceptions du moteur de création
    des événements de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""


class CreationEvenementError(Exception):
    """
    Exception de base du moteur de création.
    """
    pass


class CreatorIntrouvableError(
    CreationEvenementError,
):
    """
    Aucun Creator n'est enregistré
    pour ce type d'événement.
    """
    pass


class DonneesEvenementInvalidesError(
    CreationEvenementError,
):
    """
    Les données nécessaires à la création
    de l'événement sont invalides
    ou incomplètes.
    """
    pass


class CreationImpossibleError(
    CreationEvenementError,
):
    """
    Une erreur est survenue lors
    de la création de l'événement.
    """
    pass