"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/reintegration.py

Description :
    Handler de réintégration.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models.reintegration import (
    Reintegration,
)

from apps.rh.services.evenements.handlers.base_statut import (
    BaseStatutHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    creer_situation,
)


class ReintegrationHandler(
    BaseStatutHandler,
):
    """
    Handler de réintégration.

    Conséquences métier :

        - clôture de la situation administrative
          courante ;

        - création d'une nouvelle situation
          administrative.

    L'affectation et l'occupation de poste
    restent inchangées.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.reintegration = (
            self.get_evenement_data(
                "reintegration",
                Reintegration,
            )
        )

    def create_situation(self):
        """
        Crée la nouvelle situation
        administrative.
        """

        return creer_situation(

            agent=self.agent,

            source=self.reintegration,

            evenement=self.evenement,

            date_effet=self.date_effet,

        )

    def process(self):
        """
        Exécute la réintégration.
        """

        situation = (
            self.update_situation()
        )

        return {
            "evenement": self.evenement,
            "situation": situation,
        }


HandlerRegistry.register(
    "REINTEGRATION",
    ReintegrationHandler,
)