# apps/rh/services/evenements/handlers/base_affectation.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/base_affectation.py

Description :
    Classe de base des handlers modifiant
    l'affectation d'un agent.

Auteur : SGCP
Version : 2.1
==========================================================
"""

from abc import abstractmethod
from datetime import timedelta

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.exceptions import (
    AffectationError,
)

from apps.rh.services.evenements.utils import (
    cloturer_affectation,
    cloturer_occupation,
)


class BaseAffectationHandler(
    BaseEvenementHandler,
):
    """
    Classe de base des événements modifiant
    l'affectation d'un agent.

    Cette classe mutualise les traitements
    communs aux événements suivants :

        - Affectation
        - Mutation

    Les données spécialisées sont créées
    lors de la création de l'événement.

    Le handler se contente de rendre
    l'affectation effective.
    """

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):
        """
        Validation commune.
        """

        super().validate()

        if self.affectation is None:
            raise AffectationError(
                "Aucune affectation courante "
                "n'a été trouvée."
            )

    # =====================================================
    # Traitements communs
    # =====================================================

    def update_affectation(self):
        """
        Clôture l'affectation courante
        puis rend effective la nouvelle.
        """

        cloturer_affectation(
            self.affectation,
        )

        return self.activate_affectation()

    def update_occupation(self):
        """
        Clôture l'occupation principale
        puis crée la nouvelle.

        Les occupations d'intérim ne sont
        jamais concernées.
        """

        cloturer_occupation(
            self.occupation,
            self.date_effet - timedelta(days=1),
        )

        return self.create_occupation()

    # =====================================================
    # Méthodes à implémenter
    # =====================================================

    @abstractmethod
    def activate_affectation(self):
        """
        Rend effective l'affectation
        préparée lors de la création
        de l'événement.
        """
        raise NotImplementedError

    def create_occupation(self):
        """
        Crée la nouvelle occupation
        de poste.

        Retourne None lorsqu'aucun poste
        n'est concerné.
        """

        return None