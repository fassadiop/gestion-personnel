"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/nomination.py

Description :
    Handler de nomination.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.nomination import Nomination

from apps.rh.services.evenements.exceptions import (
    EvenementInvalideError,
)
from apps.rh.services.evenements.handlers.base_statut import (
    BaseStatutHandler,
)
from apps.rh.services.evenements.registry import HandlerRegistry
from apps.rh.services.evenements.utils import (
    creer_situation,
)


class NominationHandler(BaseStatutHandler):
    """
    Handler de nomination.

    Une nomination produit une nouvelle
    situation administrative.

    Conséquences métier :

        - clôture de la situation administrative
          actuellement en vigueur ;
        - création d'une nouvelle situation
          administrative.

    La nomination ne modifie pas directement
    l'affectation ni l'occupation du poste.
    """

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):
        """
        Validation spécifique à la nomination.
        """

        super().validate()

        self.nomination = self.load_evenement_data(
            "nomination",
            Nomination,
        )

    # =====================================================
    # Création de la nouvelle situation
    # =====================================================

    def create_new_situation(self):
        """
        Crée la nouvelle situation administrative
        résultant de la nomination.
        """

        return creer_situation(
            agent=self.agent,
            source=self.nomination,
            date_effet=self.date_effet,
            evenement=self.evenement,
        )


HandlerRegistry.register(
    "NOMINATION",
    NominationHandler,
)