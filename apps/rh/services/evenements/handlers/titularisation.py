"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/titularisation.py

Description :
    Handler de titularisation.

Auteur : SGCP
Version : 2.1
==========================================================
"""

from apps.rh.models.titularisation import (
    Titularisation,
)

from apps.rh.services.evenements.handlers.base_statut import (
    BaseStatutHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    creer_situation,
)


class TitularisationHandler(
    BaseStatutHandler,
):
    """
    Handler de titularisation.

    Conséquences métier :

        - clôture de la situation administrative
          courante ;

        - création d'une nouvelle situation
          administrative.

    L'affectation et l'occupation de poste
    restent inchangées.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.titularisation = (
            self.get_evenement_data(
                "titularisation",
                Titularisation,
            )
        )

    def create_situation(self):
        """
        Crée la nouvelle situation
        administrative.
        """

        return creer_situation(

            agent=self.agent,

            source=self.titularisation,

            situation_courante=self.situation,

            evenement=self.evenement,

            date_effet=self.date_effet,

        )

    def process(self):
        """
        Exécute la titularisation.
        """

        situation = self.update_situation()

        return {
            "evenement": self.evenement,
            "situation": situation,
        }


HandlerRegistry.register(
    "TITULARISATION",
    TitularisationHandler,
)