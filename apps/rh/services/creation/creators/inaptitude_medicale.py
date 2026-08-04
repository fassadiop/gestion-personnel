# apps/rh/services/creation/creators/inaptitude_medicale.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/inaptitude_medicale.py

Description :
    Creator de l'inaptitude médicale.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.inaptitude_medicale import (
    InaptitudeMedicale,
)

from apps.rh.services.creation.base import (
    BaseEvenementCreator,
)

from apps.rh.services.creation.registry import (
    CreationRegistry,
)

from apps.rh.models.referentiels import TypeInaptitudeMedicale


class InaptitudeMedicaleCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'inaptitude médicale.
    """

    model = InaptitudeMedicale

    key = "inaptitude_medicale"

    def process(self):
        """
        Crée la fiche spécialisée
        de l'inaptitude médicale.
        """

        data = self.payload[
            "inaptitude_medicale"
        ]

        type_inaptitude = TypeInaptitudeMedicale.objects.get(
            pk=data["type_inaptitude"]
        )

        InaptitudeMedicale.objects.create(

            evenement=self.evenement,

            type_inaptitude=type_inaptitude,

            date_effet=data[
                "date_effet"
            ],

            date_fin=data.get(
                "date_fin",
            ),

            observation=data.get(
                "observation",
                "",
            ),
        )


CreationRegistry.register(
    "INAPTITUDE_MEDICALE",
    InaptitudeMedicaleCreator,
)