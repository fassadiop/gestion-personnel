"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/prise_service_affectation.py

Description :
    Handler de la prise de service après
    affectation.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models.prise_service_affectation import (
    PriseServiceAffectation,
)

from apps.rh.services.evenements.handlers.base_affectation import (
    BaseAffectationHandler,
)

from apps.rh.services.evenements.exceptions import (
    AffectationError,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    creer_affectation,
)


class PriseServiceAffectationHandler(
    BaseAffectationHandler,
):
    """
    Handler de la prise de service après
    affectation.

    Conséquences métier :

        - clôture de l'affectation courante ;

        - création d'une nouvelle affectation.

    La situation administrative et
    l'occupation de poste restent inchangées.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.affectation is None:
            raise AffectationError(
                "Aucune affectation active à remplacer."
            )

        self.prise_service_affectation = (
            self.get_evenement_data(
                "prise_service_affectation",
                PriseServiceAffectation,
            )
        )

    def create_affectation(self):
        """
        Crée la nouvelle affectation.
        """

        return creer_affectation(

            agent=self.agent,

            source=self.prise_service_affectation,

            evenement=self.evenement,

        )

    def process(self):
        """
        Exécute la prise de service après
        affectation.
        """

        affectation = (
            self.update_affectation()
        )

        return {
            "evenement": self.evenement,
            "affectation": affectation,
        }


HandlerRegistry.register(
    "PRISE_SERVICE_AFFECTATION",
    PriseServiceAffectationHandler,
)