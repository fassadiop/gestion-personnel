"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/recrutement.py

Description :
    Handler du recrutement.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models.recrutement import Recrutement

from apps.rh.models.referentiels import PositionAdministrative
from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.exceptions import (
    SituationAdministrativeError,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    creer_situation,
)


class RecrutementHandler(BaseEvenementHandler):
    """
    Handler du recrutement.

    Le recrutement constitue le premier
    événement de carrière d'un agent.

    Conséquence métier :

        - création de la première SituationAdministrative.

    L'affectation et l'occupation de poste seront créées
    lors de la Prise de service initiale.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.situation:
            raise SituationAdministrativeError(
                "L'agent possède déjà une situation "
                "administrative en cours."
            )

        self.recrutement = (
            self.get_evenement_data(
                "recrutement",
                Recrutement,
            )
        )

    def process(self):
        """
        Exécute le recrutement.
        """

        situation = creer_situation(

            agent=self.agent,

            source=self.recrutement,

            evenement=self.evenement,

            date_effet=self.date_effet,

        )

        return {
            "evenement": self.evenement,
            "situation": situation,
        }


HandlerRegistry.register(
    "RECRUTEMENT",
    RecrutementHandler,
)