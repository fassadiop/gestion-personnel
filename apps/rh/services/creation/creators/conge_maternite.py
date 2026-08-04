"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/conge_maternite.py

Description :
    Creator du congé de maternité.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.conge_maternite import (
    CongeMaternite,
)

from apps.rh.services.creation.base import (
    BaseEvenementCreator,
)

from apps.rh.services.creation.registry import (
    CreationRegistry,
)

class CongeMaterniteCreator(BaseEvenementCreator):
    """
    Creator du congé de maternité.
    """

    model = CongeMaternite

    key = "conge_maternite"

    def process(self):
        data = self.payload["conge_maternite"]

        CongeMaternite.objects.create(
            evenement=self.evenement,
            date_debut=data["date_debut"],
            date_fin=data["date_fin"],
        )


CreationRegistry.register(
    "CONGE_MATERNITE",
    CongeMaterniteCreator,
)