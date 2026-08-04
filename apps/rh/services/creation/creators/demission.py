"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/demission.py

Description :
    Creator de l'événement Démission.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.services.creation.base import (
    BaseEvenementCreator,
)

from apps.rh.services.creation.exceptions import (
    DonneesEvenementInvalidesError,
)

from apps.rh.services.creation.registry import (
    CreationRegistry,
)

from apps.rh.services.creation.utils import (
    creer_demission,
)


class DemissionCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Démission.
    """

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.demission = (
            self.payload.get(
                "demission"
            )
        )

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.demission is None:
            raise DonneesEvenementInvalidesError(
                "Les informations de la démission sont obligatoires."
            )

        champs_obligatoires = [
            "motif",

        ]

        for champ in champs_obligatoires:

            if self.demission.get(champ) is None:

                raise DonneesEvenementInvalidesError(
                    f"Le champ '{champ}' est obligatoire."
                )

    def process(self):
        """
        Crée la fiche spécialisée.
        """

        creer_demission(

            evenement=self.evenement,

            motif=self.demission.get(
                "motif"
            ),
        )


CreationRegistry.register(
    "DEMISSION",
    DemissionCreator,
)