"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/fin_interim.py

Description :
    Handler de fin d'intérim.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models.fin_interim import (
    FinInterim,
)

from apps.rh.models.occupation import (
    OccupationPoste,
)

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.exceptions import (
    OccupationPosteError,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    cloturer_occupation,
)


class FinInterimHandler(
    BaseEvenementHandler,
):
    """
    Handler de fin d'intérim.

    Conséquence métier :

        - clôture de l'occupation
          d'intérim.

    La situation administrative,
    l'affectation et l'occupation
    principale restent inchangées.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.fin_interim = (
            self.get_evenement_data(
                "fin_interim",
                FinInterim,
            )
        )

        self.occupation_interim = (
            OccupationPoste.objects.filter(
                agent=self.agent,
                est_interim=True,
                date_fin__isnull=True,
            )
            .order_by("-date_debut")
            .first()
        )

        if self.occupation_interim is None:
            raise OccupationPosteError(
                "Aucun intérim actif n'a été trouvé."
            )

    def process(self):
        """
        Exécute la fin d'intérim.
        """

        cloturer_occupation(
            self.occupation_interim,
            self.fin_interim.date_fin_interim,
        )

        return {
            "evenement": self.evenement,
            "occupation": self.occupation_interim,
        }


HandlerRegistry.register(
    "FIN_INTERIM",
    FinInterimHandler,
)