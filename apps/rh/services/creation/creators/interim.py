"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/interim.py

Description :
    Creator de l'événement Intérim.

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
    creer_interim,
)


class InterimCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Intérim.
    """

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.interim = (
            self.payload.get(
                "interim"
            )
        )

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.interim is None:
            raise DonneesEvenementInvalidesError(
                "Les informations de l'intérim sont obligatoires."
            )

        champs_obligatoires = [

            "poste",

        ]

        for champ in champs_obligatoires:

            if self.interim.get(champ) is None:

                raise DonneesEvenementInvalidesError(
                    f"Le champ '{champ}' est obligatoire."
                )

    def process(self):
        """
        Crée la fiche spécialisée.
        """

        creer_interim(

            evenement=self.evenement,

            poste=self.interim[
                "poste"
            ],
        )


CreationRegistry.register(
    "INTERIM",
    InterimCreator,
)