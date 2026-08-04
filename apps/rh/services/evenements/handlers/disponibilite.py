"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/disponibilite.py

Description :
    Handler de disponibilité.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.disponibilite import (
    Disponibilite,
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


class DisponibiliteHandler(
    BaseSortieTemporaireHandler,
):
    """
    Handler de disponibilité.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.disponibilite = (
            self.get_evenement_data(
                "disponibilite",
                Disponibilite,
            )
        )

    def create_situation(self):
        """
        Crée la nouvelle situation
        administrative.
        """

        return creer_situation(

            agent=self.agent,

            source=self.disponibilite,

            situation_courante=self.situation,

            evenement=self.evenement,

            date_effet=self.date_effet,
        )


HandlerRegistry.register(
    "DISPONIBILITE",
    DisponibiliteHandler,
)