"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/conge.py

Description :
    Creator du congé.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Conge,
    DecisionConge,
)

from apps.rh.services.creation.base import (
    BaseEvenementCreator,
)

from apps.rh.services.creation.registry import (
    CreationRegistry,
)


class CongeCreator(
    BaseEvenementCreator,
):
    """
    Creator du congé.
    """

    model = Conge

    key = "conge"

    def process(self):
        """
        Crée la fiche spécialisée
        du congé.
        """

        data = self.payload["conge"]

        Conge.objects.create(

            evenement=self.evenement,

            decision_conge=DecisionConge.objects.get(
                pk=data["decision_conge"]
            ),

            date_cessation_service=data[
                "date_cessation_service"
            ],

            date_reprise=data[
                "date_reprise"
            ],

            observation=data.get(
                "observation",
                "",
            ),
        )


CreationRegistry.register(
    "CONGE",
    CongeCreator,
)