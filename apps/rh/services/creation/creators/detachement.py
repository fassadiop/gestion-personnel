"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/detachement.py

Description :
    Creator de l'événement Détachement.

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
    creer_detachement,
)


class DetachementCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Détachement.
    """

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.detachement = (
            self.payload.get(
                "detachement"
            )
        )

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.detachement is None:
            raise DonneesEvenementInvalidesError(
                "Les informations du détachement sont obligatoires."
            )

        champs_obligatoires = [

            "date_debut",

        ]

        for champ in champs_obligatoires:

            if self.detachement.get(champ) is None:

                raise DonneesEvenementInvalidesError(
                    f"Le champ '{champ}' est obligatoire."
                )

    def process(self):
        """
        Crée la fiche spécialisée.
        """

        creer_detachement(

            evenement=self.evenement,

            organisme_accueil=self.detachement.get(
                "organisme_accueil"
            ),

            structure=self.detachement.get(
                "structure"
            ),

            unite=self.detachement.get(
                "unite"
            ),

            date_debut=self.detachement.get(
                "date_debut"
            ),

            date_fin=self.detachement.get(
                "date_fin"
            ),
        )


CreationRegistry.register(
    "DETACHEMENT",
    DetachementCreator,
)