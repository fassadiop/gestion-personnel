"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/radiation.py

Description :
    Handler de radiation.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.radiation import (
    Radiation,
)

from apps.rh.services.evenements.handlers.base_sortie_definitive import (
    BaseSortieDefinitiveHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    creer_situation,
)


class RadiationHandler(
    BaseSortieDefinitiveHandler,
):
    """
    Handler de radiation.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.radiation = (
            self.get_evenement_data(
                "radiation",
                Radiation,
            )
        )

    def create_situation(self):
        """
        Crée la nouvelle situation
        administrative.
        """

        return creer_situation(

            agent=self.agent,

            source=self.radiation,

            situation_courante=self.situation,

            evenement=self.evenement,

            date_effet=self.date_effet,
        )



HandlerRegistry.register(
    "RADIATION",
    RadiationHandler,
)