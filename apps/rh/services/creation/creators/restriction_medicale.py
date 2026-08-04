"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/restriction_medicale.py

Description :
    Creator de la restriction médicale.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.restriction_medicale import (
    RestrictionMedicale,
)

from apps.rh.services.creation.base import (
    BaseEvenementCreator,
)

from apps.rh.services.creation.registry import (
    CreationRegistry,
)


class RestrictionMedicaleCreator(
    BaseEvenementCreator,
):
    """
    Creator de la restriction médicale.
    """

    model = RestrictionMedicale

    key = "restriction_medicale"

    def process(self):
        """
        Crée la fiche spécialisée
        de la restriction médicale.
        """

        data = self.payload[
            "restriction_medicale"
        ]

        RestrictionMedicale.objects.create(

            evenement=self.evenement,

            date_effet=data[
                "date_effet"
            ],

            date_fin=data.get(
                "date_fin",
            ),

            restriction=data[
                "restriction"
            ],

            observation=data.get(
                "observation",
                "",
            ),
        )


CreationRegistry.register(
    "RESTRICTION_MEDICALE",
    RestrictionMedicaleCreator,
)