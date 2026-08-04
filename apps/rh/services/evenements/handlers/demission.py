"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/demission.py

Description :
    Handler de démission.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.demission import (
    Demission,
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


class DemissionHandler(
    BaseSortieDefinitiveHandler,
):
    """
    Handler de démission.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.demission = (
            self.get_evenement_data(
                "demission",
                Demission,
            )
        )

    def create_situation(self):
        """
        Crée la nouvelle situation
        administrative.
        """

        return creer_situation(

            agent=self.agent,

            source=self.demission,

            situation_courante=self.situation,

            evenement=self.evenement,

            date_effet=self.date_effet,
        )


HandlerRegistry.register(
    "DEMISSION",
    DemissionHandler,
)