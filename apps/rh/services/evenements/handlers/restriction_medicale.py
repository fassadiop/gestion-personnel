"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/restriction_medicale.py

Description :
    Handler de la restriction médicale.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.restriction_medicale import (
    RestrictionMedicale,
)

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)


class RestrictionMedicaleHandler(
    BaseEvenementHandler,
):
    """
    Handler de la restriction médicale.
    """

    def validate(self):
        """
        Valide les données métier.
        """

        super().validate()

        self.restriction_medicale = (
            self.get_evenement_data(
                "restriction_medicale",
                RestrictionMedicale,
            )
        )

    def process(self):
        """
        Retourne les informations
        de la restriction médicale.
        """

        return {

            "evenement": self.evenement,

            "restriction_medicale": (
                self.restriction_medicale
            ),

        }


HandlerRegistry.register(
    "RESTRICTION_MEDICALE",
    RestrictionMedicaleHandler,
)