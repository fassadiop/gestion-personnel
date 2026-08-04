# apps/rh/services/evenements/handlers/base_statut.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/base_statut.py

Description :
    Classe de base des handlers modifiant la
    situation administrative d'un agent.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from abc import abstractmethod
from datetime import timedelta

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.exceptions import (
    SituationAdministrativeError,
)

from apps.rh.services.evenements.utils import (
    cloturer_situation,
)


class BaseStatutHandler(
    BaseEvenementHandler,
):
    """
    Classe de base des événements modifiant
    la situation administrative d'un agent.

    Cette classe mutualise les traitements
    communs aux événements suivants :

        - Titularisation
        - Nomination
        - Reclassement
        - Mise à disposition
        - Détachement
        - Réintégration
        - Disponibilité
        - Démission
        - Radiation
        - Retraite

    Le recrutement n'utilise pas cette classe
    puisqu'il ne possède pas de situation
    administrative à clôturer.
    """

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):
        """
        Validation commune.
        """

        super().validate()

        if self.situation is None:
            raise SituationAdministrativeError(
                "Aucune situation administrative "
                "courante n'a été trouvée."
            )

    # =====================================================
    # Traitement
    # =====================================================

    def update_situation(self):
        """
        Clôture la situation administrative
        courante puis crée la nouvelle.
        """

        cloturer_situation(
            self.situation,
            self.date_effet - timedelta(days=1),
        )

        return self.create_situation()

    # =====================================================
    # Méthodes à implémenter
    # =====================================================

    @abstractmethod
    def create_situation(self):
        """
        Crée la nouvelle situation
        administrative.
        """
        raise NotImplementedError