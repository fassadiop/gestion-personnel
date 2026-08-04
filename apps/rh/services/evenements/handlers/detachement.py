"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/detachement.py

Description :
    Handler de détachement.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.detachement import (
    Detachement,
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


class DetachementHandler(
    BaseSortieTemporaireHandler,
):
    """
    Handler de détachement.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.detachement = (
            self.get_evenement_data(
                "detachement",
                Detachement,
            )
        )

    def create_situation(self):
        """
        Crée la nouvelle situation
        administrative.
        """

        return creer_situation(

            agent=self.agent,

            source=self.detachement,

            situation_courante=self.situation,

            evenement=self.evenement,

            date_effet=self.date_effet,
        )


HandlerRegistry.register(
    "DETACHEMENT",
    DetachementHandler,
)