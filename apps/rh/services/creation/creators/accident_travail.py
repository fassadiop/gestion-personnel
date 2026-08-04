"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/accident_travail.py

Description :
    Creator de l'accident de travail.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.accident_travail import (
    AccidentTravail,
)

from apps.rh.services.creation.base import (
    BaseEvenementCreator,
)

from apps.rh.services.creation.registry import (
    CreationRegistry,
)


class AccidentTravailCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'accident de travail.
    """

    model = AccidentTravail

    key = "accident_travail"

    def process(self):
        """
        Crée la fiche spécialisée
        de l'accident de travail.
        """

        data = self.payload[
            "accident_travail"
        ]

        AccidentTravail.objects.create(

            evenement=self.evenement,

            date_accident=data[
                "date_accident"
            ],

            lieu_accident=data[
                "lieu_accident"
            ],

            circonstances=data[
                "circonstances"
            ],

            consequences=data.get(
                "consequences",
                "",
            ),

            observation=data.get(
                "observation",
                "",
            ),
        )


CreationRegistry.register(
    "ACCIDENT_TRAVAIL",
    AccidentTravailCreator,
)