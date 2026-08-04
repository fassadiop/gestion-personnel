"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/context.py

Description :
    Contexte d'exécution du moteur
    de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""


class ExecutionContext:
    """
    Contexte partagé entre le service
    d'exécution et les handlers.

    Il centralise toutes les informations
    nécessaires au traitement d'un
    événement de carrière.
    """

    def __init__(
        self,
        *,
        evenement,
        utilisateur=None,
        request=None,
    ):
        """
        Initialise le contexte
        d'exécution.
        """

        self.evenement = evenement

        self.utilisateur = utilisateur

        self.request = request