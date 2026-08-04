"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/reclassement.py

Description :
    Handler de validation d'un reclassement.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models.reclassement import Reclassement

from apps.rh.services.evenements.handlers.base_statut import (
    BaseStatutHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    creer_situation,
)


class ReclassementHandler(BaseStatutHandler):
    """
    Handler de validation d'un reclassement.

    Conséquences métier :

        - clôture de la situation administrative active ;

        - création d'une nouvelle situation administrative
          avec le nouveau grade, la nouvelle classe
          et le nouvel échelon.

    Le reclassement ne modifie ni l'affectation,
    ni l'occupation du poste.
    """

    def validate(self):
        """
        Valide les données nécessaires au reclassement.
        """

        super().validate()

        self.reclassement = self.get_evenement_data(
            relation_name="reclassement",
            model_class=Reclassement,
        )

    def create_situation(self):
        """
        Crée la nouvelle situation administrative.
        """

        return creer_situation(
            agent=self.agent,
            situation_courante=self.situation,
            source=self.reclassement,
            evenement=self.evenement,
            date_effet=self.date_effet,
        )

    def process(self):
        """
        Exécute le reclassement.
        """

        situation = self.update_situation()

        return {
            "evenement": self.evenement,
            "situation": situation,
        }


HandlerRegistry.register(
    "RECLASSEMENT",
    ReclassementHandler,
)