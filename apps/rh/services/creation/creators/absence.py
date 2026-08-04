"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/absence.py

Description :
    Creator de l'autorisation d'absence.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Absence,
    TypeAbsence,
)

from apps.rh.services.creation.base import (
    BaseEvenementCreator,
)

from apps.rh.services.creation.registry import (
    CreationRegistry,
)


class AbsenceCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'autorisation d'absence.
    """

    model = Absence

    key = "absence"

    def process(self):
        """
        Crée la fiche spécialisée
        de l'autorisation d'absence.
        """

        data = self.payload["absence"]

        Absence.objects.create(

            evenement=self.evenement,

            type_absence=TypeAbsence.objects.get(
                pk=data["type_absence"]
            ),

            date_debut=data[
                "date_debut"
            ],

            date_fin=data[
                "date_fin"
            ],

            jours_deductibles=data.get(
                "jours_deductibles",
                0,
            ),

            motif=data.get(
                "motif",
                "",
            ),

            observation=data.get(
                "observation",
                "",
            ),
        )


CreationRegistry.register(
    "ABSENCE",
    AbsenceCreator,
)