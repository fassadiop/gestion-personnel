"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/conge_maladie.py

Description :
    Handler du congé de maladie.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from builtins import super

from apps.rh.models.conge_maladie import (
    CongeMaladie,
)

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)


class CongeMaladieHandler(
    BaseEvenementHandler,
):
    """
    Handler du congé de maladie.
    """

    def validate(self):

        super().validate()

        self.conge_maladie = (
            self.get_evenement_data(
                "conge_maladie",
                CongeMaladie,
            )
        )

    def process(self):

        return {

            "evenement": self.evenement,

            "conge_maladie": self.conge_maladie,

        }


HandlerRegistry.register(
    "CONGE_MALADIE",
    CongeMaladieHandler,
)