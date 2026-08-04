"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/affectation.py

Description :
    Handler d'affectation.

Auteur : SGCP
Version : 2.1
==========================================================
"""

from apps.rh.models.affectation import (
    Affectation as AffectationEvenement,
)

from apps.rh.services.evenements.base import BaseEvenementHandler
from apps.rh.services.evenements.handlers.base_affectation import (
    BaseAffectationHandler,
)

from apps.rh.services.evenements.exceptions import (
    EvenementInvalideError,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    creer_occupation,
)


class AffectationHandler(
    BaseAffectationHandler,
):
    """
    Handler d'affectation.

    Conséquences métier :

        - clôture de l'affectation courante ;

        - activation de l'affectation
          préparée lors de la création
          de l'événement.

    La situation administrative et
    l'occupation de poste restent inchangées.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        BaseEvenementHandler.validate(self)

        self.affectation_evenement = (
            self.get_evenement_data(
                "affectation",
                AffectationEvenement,
            )
        )

        if (
            self.affectation_evenement.structure
            is None
        ):
            raise EvenementInvalideError(
                "La structure est obligatoire."
            )

    def activate_affectation(self):
        """
        Rend effective l'affectation
        préparée lors de la création
        de l'événement.
        """

        self.affectation_evenement.est_courante = True

        self.affectation_evenement.save(
            update_fields=[
                "est_courante",
                "updated_at",
            ]
        )

        return self.affectation_evenement

    def create_occupation(self):
        """
        Crée l'occupation de poste correspondant
        à l'affectation.

        Retourne None lorsqu'aucun poste
        n'est renseigné.
        """

        return creer_occupation(
            agent=self.agent,
            poste=self.affectation_evenement.poste,
            evenement=self.evenement,
            date_debut=self.date_effet,
        )

    def process(self):
        """
        Exécute l'affectation.
        """

        if self.affectation is None:

            affectation = self.activate_affectation()

        else:

            affectation = self.update_affectation()

        occupation = None

        if self.affectation_evenement.poste is not None:

            occupation = self.update_occupation()

        return {
            "evenement": self.evenement,
            "affectation": affectation,
            "occupation": occupation,
        }


HandlerRegistry.register(
    "AFFECTATION",
    AffectationHandler,
)