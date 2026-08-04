"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/mise_a_disposition.py

Description :
    Handler de mise à disposition.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.mise_a_disposition import (
    MiseADisposition,
)

from apps.rh.services.evenements.handlers.base_sortie_temporaire import (
    BaseSortieTemporaireHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    creer_situation,
)


class MiseADispositionHandler(
    BaseSortieTemporaireHandler,
):
    """
    Handler de mise à disposition.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.mise_a_disposition = (
            self.get_evenement_data(
                "mise_a_disposition",
                MiseADisposition,
            )
        )

    def create_situation(self):
        """
        Crée la nouvelle situation
        administrative.
        """

        return creer_situation(

            agent=self.agent,

            source=self.mise_a_disposition,

            situation_courante=self.situation,

            evenement=self.evenement,

            date_effet=self.date_effet,
        )


HandlerRegistry.register(
    "MISE_DISPOSITION",
    MiseADispositionHandler,
)