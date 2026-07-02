"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/reclassement.py

Description :
    Handler de reclassement.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.reclassement import Reclassement

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


class ReclassementHandler(BaseStatutHandler):
    """
    Handler de reclassement.

    Le reclassement crée une nouvelle situation
    administrative tout en conservant
    l'affectation actuelle de l'agent.
    """

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):
        """
        Validation spécifique au reclassement.
        """

        super().validate()

        self.reclassement = self.load_evenement_data(
            "reclassement",
            Reclassement,
        )

    # =====================================================
    # Nouvelle situation
    # =====================================================

    def create_new_situation(self):
        """
        Crée la nouvelle situation administrative.
        """

        return creer_situation(
            agent=self.agent,
            source=self.reclassement,
            date_effet=self.date_effet,
            evenement=self.evenement,
        )


HandlerRegistry.register(
    "RECLASSEMENT",
    ReclassementHandler,
)