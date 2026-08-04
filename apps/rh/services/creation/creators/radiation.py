"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/radiation.py

Description :
    Creator de l'événement Radiation.

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
    creer_radiation,
)


class RadiationCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Radiation.
    """

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.radiation = (
            self.payload.get(
                "radiation"
            )
        )

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.radiation is None:
            raise DonneesEvenementInvalidesError(
                "Les informations de la radiation sont obligatoires."
            )

        champs_obligatoires = [
            "motif",

        ]

        for champ in champs_obligatoires:

            if self.radiation.get(champ) is None:

                raise DonneesEvenementInvalidesError(
                    f"Le champ '{champ}' est obligatoire."
                )

    def process(self):
        """
        Crée la fiche spécialisée.
        """

        creer_radiation(

            evenement=self.evenement,

            motif=self.radiation.get(
                "motif"
            ),
        )


CreationRegistry.register(
    "RADIATION",
    RadiationCreator,
)