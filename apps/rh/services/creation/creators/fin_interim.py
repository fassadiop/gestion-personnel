"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/fin_interim.py

Description :
    Creator de l'événement Fin d'intérim.

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
    creer_fin_interim,
)


class FinInterimCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Fin d'intérim.
    """

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.fin_interim = (
            self.payload.get(
                "fin_interim"
            )
        )

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.fin_interim is None:
            raise DonneesEvenementInvalidesError(
                "Les informations de fin d'intérim sont obligatoires."
            )

        if (
            self.fin_interim.get(
                "date_fin_interim"
            )
            is None
        ):
            raise DonneesEvenementInvalidesError(
                "Le champ 'date_fin_interim' est obligatoire."
            )

    def process(self):
        """
        Crée la fiche spécialisée.
        """

        creer_fin_interim(

            evenement=self.evenement,

            date_fin_interim=self.fin_interim[
                "date_fin_interim"
            ],
        )


CreationRegistry.register(
    "FIN_INTERIM",
    FinInterimCreator,
)