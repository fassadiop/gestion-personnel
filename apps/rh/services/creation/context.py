"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/context.py

Description :
    Contexte d'exécution du moteur de création
    des événements de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""


class CreationContext:
    """
    Contexte partagé entre les différents
    composants du moteur de création.

    Il transporte toutes les informations
    nécessaires durant le cycle de création
    d'un événement.
    """

    def __init__(
        self,
        *,
        validated_data,
        payload,
        utilisateur=None,
        request=None,
    ):
        """
        Initialise le contexte.
        """

        # ==============================
        # Données validées
        # ==============================

        self.validated_data = validated_data

        # ==============================
        # Payload HTTP complet
        # ==============================

        self.payload = payload

        # ==============================
        # Utilisateur courant
        # ==============================

        self.utilisateur = utilisateur

        # ==============================
        # Requête HTTP
        # ==============================

        self.request = request

        # ==============================
        # Objet créé par le moteur
        # ==============================

        self.evenement = None