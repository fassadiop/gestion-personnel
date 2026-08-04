"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/reprise_service.py

Description :
    Handler de la reprise de service.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.reprise_service import (
    RepriseService,
)

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)


class RepriseServiceHandler(
    BaseEvenementHandler,
):
    """
    Handler de la reprise de service.
    """

    def validate(self):
        """
        Valide les données métier.
        """

        super().validate()

        self.reprise_service = (
            self.get_evenement_data(
                "reprise_service",
                RepriseService,
            )
        )

    def process(self):
        """
        Traite la reprise de service.
        """

        return {

            "evenement": self.evenement,

            "reprise_service": (
                self.reprise_service
            ),

        }


HandlerRegistry.register(
    "REPRISE_SERVICE",
    RepriseServiceHandler,
)