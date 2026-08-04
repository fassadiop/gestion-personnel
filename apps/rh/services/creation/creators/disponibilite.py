"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/disponibilite.py

Description :
    Creator de l'événement Disponibilité.

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
    creer_disponibilite,
)


class DisponibiliteCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Disponibilité.
    """

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.disponibilite = (
            self.payload.get(
                "disponibilite"
            )
        )

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.disponibilite is None:
            raise DonneesEvenementInvalidesError(
                "Les informations de la disponibilité sont obligatoires."
            )

        champs_obligatoires = [

            "date_debut",

        ]

        for champ in champs_obligatoires:

            if self.disponibilite.get(champ) is None:

                raise DonneesEvenementInvalidesError(
                    f"Le champ '{champ}' est obligatoire."
                )

    def process(self):
        """
        Crée la fiche spécialisée.
        """

        creer_disponibilite(

            evenement=self.evenement,

            motif=self.disponibilite.get(
                "motif"
            ),

            date_debut=self.disponibilite.get(
                "date_debut"
            ),

            date_fin=self.disponibilite.get(
                "date_fin"
            ),
        )


CreationRegistry.register(
    "DISPONIBILITE",
    DisponibiliteCreator,
)