# apps/rh/services/evenements/handlers/conge_maternite.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/conge_maternite.py

Description :
    Handler du congé de maternité.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from builtins import super

from apps.rh.models.conge_maternite import (
    CongeMaternite,
)

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)


class CongeMaterniteHandler(
    BaseEvenementHandler,
):
    """
    Handler du congé de maternité.
    """

    def validate(self):

        super().validate()

        self.conge_maternite = (
            self.get_evenement_data(
                "conge_maternite",
                CongeMaternite,
            )
        )

    def process(self):

        return {

            "evenement": self.evenement,

            "conge_maternite": self.conge_maternite,

        }


HandlerRegistry.register(
    "CONGE_MATERNITE",
    CongeMaterniteHandler,
)