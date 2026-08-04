"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/reprise_service.py

Description :
    Creator de la reprise de service.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.reprise_service import (
    RepriseService,
)

from apps.rh.services.creation.base import (
    BaseEvenementCreator,
)

from apps.rh.services.creation.registry import (
    CreationRegistry,
)


class RepriseServiceCreator(
    BaseEvenementCreator,
):
    """
    Creator de la reprise de service.
    """

    model = RepriseService

    key = "reprise_service"

    def process(self):
        """
        Crée la fiche spécialisée
        de la reprise de service.
        """

        data = self.payload[
            "reprise_service"
        ]

        RepriseService.objects.create(

            evenement=self.evenement,

            date_reprise=data[
                "date_reprise"
            ],

            observation=data.get(
                "observation",
                "",
            ),
        )


CreationRegistry.register(
    "REPRISE_SERVICE",
    RepriseServiceCreator,
)