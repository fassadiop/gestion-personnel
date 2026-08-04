"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/retraite.py

Description :
    Handler de retraite.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.retraite import (
    Retraite,
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


class RetraiteHandler(
    BaseSortieDefinitiveHandler,
):
    """
    Handler de retraite.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.retraite = (
            self.get_evenement_data(
                "retraite",
                Retraite,
            )
        )

    def create_situation(self):
        """
        Crée la nouvelle situation
        administrative.
        """

        return creer_situation(

            agent=self.agent,

            source=self.retraite,

            situation_courante=self.situation,

            evenement=self.evenement,

            date_effet=self.date_effet,
        )


HandlerRegistry.register(
    "RETRAITE",
    RetraiteHandler,
)