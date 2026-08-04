"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/accident_travail.py

Description :
    Handler de l'accident de travail.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.accident_travail import (
    AccidentTravail,
)

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)


class AccidentTravailHandler(
    BaseEvenementHandler,
):
    """
    Handler de l'accident de travail.
    """

    def validate(self):
        """
        Valide les données métier.
        """

        super().validate()

        self.accident_travail = (
            self.get_evenement_data(
                "accident_travail",
                AccidentTravail,
            )
        )

    def process(self):
        """
        Traite l'accident de travail.
        """

        return {

            "evenement": self.evenement,

            "accident_travail": (
                self.accident_travail
            ),

        }


HandlerRegistry.register(
    "ACCIDENT_TRAVAIL",
    AccidentTravailHandler,
)