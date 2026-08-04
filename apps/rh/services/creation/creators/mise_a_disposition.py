"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/mise_a_disposition.py

Description :
    Creator de l'événement Mise à disposition.

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
    creer_mise_a_disposition,
)


class MiseADispositionCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Mise à disposition.
    """

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.mise_a_disposition = (
            self.payload.get(
                "mise_a_disposition"
            )
        )

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.mise_a_disposition is None:
            raise DonneesEvenementInvalidesError(
                "Les informations de la mise à disposition sont obligatoires."
            )

        champs_obligatoires = [

            "date_debut",

        ]

        for champ in champs_obligatoires:

            if self.mise_a_disposition.get(champ) is None:

                raise DonneesEvenementInvalidesError(
                    f"Le champ '{champ}' est obligatoire."
                )

    def process(self):
        """
        Crée la fiche spécialisée.
        """

        creer_mise_a_disposition(

            evenement=self.evenement,

            organisme_accueil=self.mise_a_disposition.get(
                "organisme_accueil"
            ),

            structure=self.mise_a_disposition.get(
                "structure"
            ),

            unite=self.mise_a_disposition.get(
                "unite"
            ),

            date_debut=self.mise_a_disposition.get(
                "date_debut"
            ),

            date_fin=self.mise_a_disposition.get(
                "date_fin"
            ),
        )


CreationRegistry.register(
    "MISE_DISPOSITION",
    MiseADispositionCreator,
)