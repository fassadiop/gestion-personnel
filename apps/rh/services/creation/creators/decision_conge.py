"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/decision_conge.py

Description :
    Creator de l'événement Décision de congé.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    TypeConge,
)

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
    creer_decision_conge,
)


class DecisionCongeCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Décision de congé.
    """

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.decision_conge = (
            self.payload.get(
                "decision_conge"
            )
        )

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.decision_conge is None:

            raise DonneesEvenementInvalidesError(
                "Les informations de la décision de congé sont obligatoires."
            )

        champs_obligatoires = (

            "type_conge",

            "nombre_jours_accordes",

        )

        for champ in champs_obligatoires:

            if self.decision_conge.get(champ) is None:

                raise DonneesEvenementInvalidesError(
                    f"Le champ '{champ}' est obligatoire."
                )

        self.type_conge = (
            TypeConge.objects.get(
                pk=self.decision_conge.get(
                    "type_conge"
                )
            )
        )

    def process(self):
        """
        Crée la fiche spécialisée.
        """

        creer_decision_conge(

            evenement=self.evenement,

            type_conge=self.type_conge,

            nombre_jours_accordes=(
                self.decision_conge.get(
                    "nombre_jours_accordes"
                )
            ),
        )


CreationRegistry.register(
    "DECISION_CONGE",
    DecisionCongeCreator,
)