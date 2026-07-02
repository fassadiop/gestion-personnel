# apps/rh/services/evenements/handlers/base_statut.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/base_statut.py

Description :
    Classe de base des handlers modifiant la
    situation administrative d'un agent.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from datetime import timedelta
from abc import abstractmethod

from apps.rh.services.evenements.base import BaseEvenementHandler
from apps.rh.services.evenements.exceptions import (
    SituationAdministrativeError,
)


class BaseStatutHandler(BaseEvenementHandler):
    """
    Classe de base des événements modifiant
    le statut administratif d'un agent.

    Cette classe mutualise les traitements
    communs aux événements tels que :

        - Titularisation
        - Promotion
        - Avancement
        - Reclassement
        - Changement de corps
        - Changement de grade

    Cycle métier :

        1. récupérer la situation courante ;
        2. la clôturer ;
        3. créer la nouvelle situation ;
        4. construire le contexte.
    """

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):
        """
        Validation commune.
        """

        super().validate()

        self.situation_courante = (
            self.agent.situation_administrative_courante
        )

        if self.situation_courante is None:
            raise SituationAdministrativeError(
                "Aucune situation administrative courante n'a été trouvée."
            )

    # =====================================================
    # Traitement
    # =====================================================

    def process(self):
        """
        Traitement générique.
        """

        ancienne = self.close_current_situation()

        nouvelle = self.create_new_situation()

        self.context.update(
            {
                "ancienne_situation": ancienne,
                "nouvelle_situation": nouvelle,
            }
        )

        return self.context

    # =====================================================
    # Méthodes communes
    # =====================================================

    def close_current_situation(self):
        """
        Clôture la situation administrative courante.
        """

        self.situation_courante.date_fin = (
            self.date_effet - timedelta(days=1)
        )

        self.situation_courante.est_courante = False

        self.situation_courante.save(
            update_fields=[
                "date_fin",
                "est_courante",
            ]
        )

        return self.situation_courante

    # =====================================================
    # Méthodes à implémenter
    # =====================================================

    @abstractmethod
    def create_new_situation(self):
        """
        Crée la nouvelle situation administrative.
        """
        raise NotImplementedError