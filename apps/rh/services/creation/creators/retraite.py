"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/retraite.py

Description :
    Creator de l'événement Retraite.

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
    creer_retraite,
)


class RetraiteCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Retraite.
    """

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.retraite = (
            self.payload.get(
                "retraite"
            )
        )

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.retraite is None:
            raise DonneesEvenementInvalidesError(
                "Les informations de la retraite sont obligatoires."
            )

        champs_obligatoires = [
            "motif",

        ]

        for champ in champs_obligatoires:

            if self.retraite.get(champ) is None:

                raise DonneesEvenementInvalidesError(
                    f"Le champ '{champ}' est obligatoire."
                )

    def process(self):
        """
        Crée la fiche spécialisée.
        """

        creer_retraite(

            evenement=self.evenement,

            motif=self.retraite.get(
                "motif"
            ),
        )


CreationRegistry.register(
    "RETRAITE",
    RetraiteCreator,
)