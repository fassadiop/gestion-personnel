"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/reclassement.py

Description :
    Creator de l'événement Reclassement.

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
    creer_reclassement,
)


class ReclassementCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Reclassement.

    Responsabilités :

        - créer l'événement de carrière ;

        - créer la fiche spécialisée
          de reclassement.

    Aucune conséquence métier n'est
    produite ici.

    Le moteur de carrière exécutera
    ultérieurement le ReclassementHandler.
    """

    # =====================================================
    # Chargement des données
    # =====================================================

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.reclassement = (
            self.payload.get(
                "reclassement"
            )
        )

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.reclassement is None:
            raise DonneesEvenementInvalidesError(
                "Les informations du reclassement sont obligatoires."
            )

        if self.reclassement.get(
            "corps"
        ) is None:
            raise DonneesEvenementInvalidesError(
                "Le corps est obligatoire."
            )

        if self.reclassement.get(
            "grade"
        ) is None:
            raise DonneesEvenementInvalidesError(
                "Le grade est obligatoire."
            )

        if self.reclassement.get(
            "classe"
        ) is None:
            raise DonneesEvenementInvalidesError(
                "La classe est obligatoire."
            )

        if self.reclassement.get(
            "echelon"
        ) is None:
            raise DonneesEvenementInvalidesError(
                "L'échelon est obligatoire."
            )

    # =====================================================
    # Traitement
    # =====================================================

    def process(self):
        """
        Crée la fiche spécialisée
        de reclassement.
        """

        creer_reclassement(

            evenement=self.evenement,

            corps=self.reclassement["corps"],

            grade=self.reclassement["grade"],

            classe=self.reclassement["classe"],

            echelon=self.reclassement["echelon"],
        )


CreationRegistry.register(
    "RECLASSEMENT",
    ReclassementCreator,
)