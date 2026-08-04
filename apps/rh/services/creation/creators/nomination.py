"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/nomination.py

Description :
    Creator de l'événement Nomination.

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
    creer_nomination,
)


class NominationCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Nomination.
    """

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.nomination = (
            self.payload.get(
                "nomination"
            )
        )

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.nomination is None:
            raise DonneesEvenementInvalidesError(
                "Les informations de la nomination sont obligatoires."
            )

        champs_obligatoires = [

            "structure",

            "poste",

        ]

        for champ in champs_obligatoires:

            if self.nomination.get(champ) is None:

                raise DonneesEvenementInvalidesError(
                    f"Le champ '{champ}' est obligatoire."
                )

    def process(self):
        """
        Crée la fiche spécialisée
        de nomination.
        """

        creer_nomination(

            evenement=self.evenement,

            structure=self.nomination[
                "structure"
            ],

            unite=self.nomination.get(
                "unite"
            ),

            poste=self.nomination[
                "poste"
            ],
        )


CreationRegistry.register(
    "NOMINATION",
    NominationCreator,
)