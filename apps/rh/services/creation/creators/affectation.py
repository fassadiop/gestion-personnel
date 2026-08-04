"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/affectation.py

Description :
    Creator de l'événement Affectation.

Auteur : SGCP
Version : 2.2
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
from apps.rh.services.creation.utils import creer_affectation


class AffectationCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Affectation.

    Responsabilités :

        - créer l'événement de carrière ;

        - créer la fiche spécialisée
          d'affectation.

    Cet événement ne modifie pas
    directement la carrière de l'agent.

    Les conséquences métier seront
    produites uniquement lors de la
    validation de l'événement par le
    moteur de carrière.
    """

    # =====================================================
    # Chargement des données
    # =====================================================

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.affectation = (
            self.payload.get(
                "affectation"
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

        if self.affectation is None:
            raise DonneesEvenementInvalidesError(
                "Les informations de l'affectation "
                "sont obligatoires."
            )

        if self.affectation.get(
            "structure"
        ) is None:
            raise DonneesEvenementInvalidesError(
                "La structure est obligatoire."
            )

    # =====================================================
    # Traitement
    # =====================================================

    def process(self):
        """
        Crée la fiche spécialisée
        d'affectation.
        """

        creer_affectation(

            evenement=self.evenement,

            agent=self.agent,

            structure=self.affectation["structure"],

            unite=self.affectation.get("unite"),

            poste=self.affectation.get("poste"),
        )


CreationRegistry.register(
    "AFFECTATION",
    AffectationCreator,
)