"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/base_sortie_definitive.py

Description :
    Classe de base des événements mettant
    fin définitivement à la carrière d'un agent.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from abc import abstractmethod
from datetime import timedelta

from apps.rh.models.occupation import (
    OccupationPoste,
)

from apps.rh.services.evenements.handlers.base_statut import (
    BaseStatutHandler,
)

from apps.rh.services.evenements.utils import (
    cloturer_affectation,
    cloturer_occupation,
)


class BaseSortieDefinitiveHandler(
    BaseStatutHandler,
):
    """
    Classe de base des événements mettant
    fin définitivement à la carrière.

    Événements concernés :

        - Démission ;

        - Retraite ;

        - Radiation.

    Conséquences métier :

        - clôture de la situation
          administrative courante ;

        - création d'une nouvelle
          situation administrative ;

        - clôture de l'affectation
          courante ;

        - clôture de l'occupation
          principale ;

        - clôture de tous les
          intérims actifs.
    """

    # =====================================================
    # Traitements communs
    # =====================================================

    def update_affectation(self):
        """
        Clôture l'affectation courante.
        """

        if self.affectation is None:
            return

        cloturer_affectation(

            self.affectation,

            self.date_effet
            - timedelta(days=1),
        )

    def update_occupation(self):
        """
        Clôture l'occupation principale.
        """

        if self.occupation is None:
            return

        cloturer_occupation(

            self.occupation,

            self.date_effet
            - timedelta(days=1),
        )

    def update_interims(self):
        """
        Clôture tous les intérims actifs.
        """

        interims = (
            OccupationPoste.objects.filter(

                agent=self.agent,

                est_interim=True,

                date_fin__isnull=True,

            )
        )

        for interim in interims:

            cloturer_occupation(

                interim,

                self.date_effet
                - timedelta(days=1),
            )

    # =====================================================
    # Traitement principal
    # =====================================================

    def process(self):
        """
        Exécute la sortie définitive.
        """

        situation = (
            self.update_situation()
        )

        self.update_affectation()

        self.update_occupation()

        self.update_interims()

        return {

            "evenement": self.evenement,

            "situation": situation,

        }

    # =====================================================
    # À implémenter
    # =====================================================

    @abstractmethod
    def create_situation(self):
        """
        Crée la nouvelle situation
        administrative.
        """
        raise NotImplementedError