"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/prise_service_initiale.py

Description :
    Handler de la prise de service initiale.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models.prise_service_initiale import (
    PriseServiceInitiale,
)

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.exceptions import (
    AffectationError,
    SituationAdministrativeError,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    creer_affectation,
)


class PriseServiceInitialeHandler(
    BaseEvenementHandler,
):
    """
    Handler de la prise de service initiale.

    Conséquence métier :

        - création de la première affectation.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.situation is None:
            raise SituationAdministrativeError(
                "L'agent ne possède aucune situation "
                "administrative active."
            )

        if self.affectation is not None:
            raise AffectationError(
                "L'agent possède déjà une "
                "affectation active."
            )

        self.prise_service_initiale = (
            self.get_evenement_data(
                "prise_service_initiale",
                PriseServiceInitiale,
            )
        )

    def process(self):
        """
        Exécute la prise de service initiale.
        """

        affectation = creer_affectation(

            agent=self.agent,

            source=self.prise_service_initiale,

            evenement=self.evenement,

        )

        return {
            "evenement": self.evenement,
            "affectation": affectation,
        }


HandlerRegistry.register(
    "PRISE_SERVICE_INITIALE",
    PriseServiceInitialeHandler,
)