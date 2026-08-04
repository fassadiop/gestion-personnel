# apps/rh/services/evenements/handlers/inaptitude_medicale.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/inaptitude_medicale.py

Description :
    Handler de l'inaptitude médicale.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from builtins import super

from apps.rh.models.inaptitude_medicale import (
    InaptitudeMedicale,
)

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)


class InaptitudeMedicaleHandler(
    BaseEvenementHandler,
):
    """
    Handler de l'inaptitude médicale.
    """

    def validate(self):

        super().validate()

        self.inaptitude_medicale = (
            self.get_evenement_data(
                "inaptitude_medicale",
                InaptitudeMedicale,
            )
        )

    def process(self):

        return {

            "evenement": self.evenement,

            "inaptitude_medicale": (
                self.inaptitude_medicale
            ),

        }


HandlerRegistry.register(
    "INAPTITUDE_MEDICALE",
    InaptitudeMedicaleHandler,
)