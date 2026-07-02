"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/titularisation.py

Description :
    Handler de titularisation.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.titularisation import Titularisation

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


class TitularisationHandler(BaseStatutHandler):
    """
    Handler de titularisation.

    La titularisation confirme définitivement
    l'intégration de l'agent dans son corps.

    Conséquences métier :

        - clôture de la situation administrative courante ;
        - création d'une nouvelle situation administrative.

    L'affectation et l'occupation du poste ne sont
    pas modifiées.
    """

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):
        """
        Validation spécifique à la titularisation.
        """

        super().validate()

        self.titularisation = self.load_evenement_data(
            "titularisation",
            Titularisation,
        )

    # =====================================================
    # Création de la nouvelle situation
    # =====================================================

    def create_new_situation(self):
        """
        Crée la nouvelle situation administrative
        de l'agent.
        """

        return creer_situation(
            agent=self.agent,
            source=self.titularisation,
            date_effet=self.date_effet,
            evenement=self.evenement,
        )


HandlerRegistry.register(
    "TITULARISATION",
    TitularisationHandler,
)