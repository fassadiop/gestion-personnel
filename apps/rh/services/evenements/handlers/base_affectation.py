"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/base_affectation.py

Description :
    Classe de base des handlers modifiant
    l'affectation d'un agent.

Auteur : SGCP
Version : 1.0
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


class BaseAffectationHandler(BaseEvenementHandler):
    """
    Classe de base des événements de mobilité.

    Cette classe mutualise les traitements communs
    aux événements modifiant l'affectation
    d'un agent.

    Exemples :

        - Affectation
        - Mutation
        - Nomination (si changement de poste)

    Cycle métier :

        1. récupérer l'affectation courante ;
        2. récupérer l'occupation du poste ;
        3. clôturer l'affectation courante ;
        4. clôturer l'occupation du poste ;
        5. créer la nouvelle affectation ;
        6. créer la nouvelle occupation ;
        7. construire le contexte.
    """

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):
        """
        Validation commune.
        """

        super().validate()

        self.affectation_courante = (
            self.agent.affectation_courante
        )

        if self.affectation_courante is None:
            raise AffectationError(
                "Aucune affectation courante n'a été trouvée."
            )

        self.occupation_courante = (
            self.agent.occupation_courante
        )

    # =====================================================
    # Traitement
    # =====================================================

    def process(self):
        """
        Traitement générique des événements
        de mobilité.
        """

        ancienne_affectation = (
            self.close_affectation()
        )

        ancienne_occupation = (
            self.close_occupation()
        )

        nouvelle_affectation = (
            self.create_new_affectation()
        )

        nouvelle_occupation = (
            self.create_new_occupation()
        )

        self.context.update(
            {
                "ancienne_affectation": ancienne_affectation,
                "ancienne_occupation": ancienne_occupation,
                "nouvelle_affectation": nouvelle_affectation,
                "nouvelle_occupation": nouvelle_occupation,
            }
        )

        return self.context

    # =====================================================
    # Méthodes communes
    # =====================================================

    def close_affectation(self):
        """
        Clôture l'affectation courante.
        """

        self.affectation_courante.date_fin = (
            self.date_effet - timedelta(days=1)
        )

        self.affectation_courante.est_courante = False

        self.affectation_courante.save(
            update_fields=[
                "date_fin",
                "est_courante",
            ]
        )

        return self.affectation_courante

    def close_occupation(self):
        """
        Clôture l'occupation courante du poste.
        """

        if self.occupation_courante is None:
            return None

        self.occupation_courante.date_fin = (
            self.date_effet - timedelta(days=1)
        )

        self.occupation_courante.save(
            update_fields=[
                "date_fin",
            ]
        )

        return self.occupation_courante

    # =====================================================
    # Méthodes à implémenter
    # =====================================================

    @abstractmethod
    def create_new_affectation(self):
        """
        Crée la nouvelle affectation.
        """
        raise NotImplementedError

    @abstractmethod
    def create_new_occupation(self):
        """
        Crée la nouvelle occupation du poste.

        Peut retourner None lorsqu'aucun poste
        n'est concerné.
        """
        raise NotImplementedError