"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/titularisation.py

Description :
    Creator de l'événement Titularisation.

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
    creer_titularisation,
)


class TitularisationCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Titularisation.
    """

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.titularisation = (
            self.payload.get(
                "titularisation"
            )
        )

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.titularisation is None:
            raise DonneesEvenementInvalidesError(
                "Les informations de la titularisation sont obligatoires."
            )

        champs_obligatoires = [

            "position_administrative",

            "grade",

            "classe",

            "echelon",

        ]

        for champ in champs_obligatoires:

            if self.titularisation.get(champ) is None:

                raise DonneesEvenementInvalidesError(
                    f"Le champ '{champ}' est obligatoire."
                )

    def process(self):
        """
        Crée la fiche spécialisée.
        """

        creer_titularisation(

            evenement=self.evenement,

            position_administrative=self.titularisation[
                "position_administrative"
            ],

            grade=self.titularisation[
                "grade"
            ],

            classe=self.titularisation[
                "classe"
            ],

            echelon=self.titularisation[
                "echelon"
            ],
        )


CreationRegistry.register(
    "TITULARISATION",
    TitularisationCreator,
)