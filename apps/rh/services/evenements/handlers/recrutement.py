"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/recrutement.py

Description :
    Handler du recrutement.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.recrutement import Recrutement

from apps.rh.services.evenements.base import BaseEvenementHandler
from apps.rh.services.evenements.exceptions import (
    EvenementInvalideError,
    SituationAdministrativeError,
)
from apps.rh.services.evenements.registry import HandlerRegistry
from apps.rh.services.evenements.utils import (
    creer_affectation,
    creer_occupation,
    creer_situation,
)


class RecrutementHandler(BaseEvenementHandler):
    """
    Handler du recrutement.

    Le recrutement constitue le premier événement
    de carrière d'un agent.

    Conséquences métier :

        - création de la première SituationAdministrative ;
        - création de la première Affectation ;
        - création éventuelle de la première OccupationPoste.
    """

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):
        """
        Validation spécifique au recrutement.
        """

        super().validate()

        if self.agent.situation_administrative_courante:
            raise SituationAdministrativeError(
                "L'agent possède déjà une situation administrative en cours."
            )

        self.recrutement = self.load_evenement_data(
            "recrutement",
            Recrutement,
        )

    # =====================================================
    # Traitement métier
    # =====================================================

    def process(self):
        """
        Exécute le recrutement.
        """

        situation = self._create_situation()

        affectation = self._create_affectation()

        occupation = self._create_occupation()

        self.context.update(
            {
                "situation": situation,
                "affectation": affectation,
                "occupation": occupation,
            }
        )

        return self.context

    # =====================================================
    # Méthodes privées
    # =====================================================

    def _create_situation(self):
        """
        Crée la première situation administrative.
        """

        return creer_situation(
            agent=self.agent,
            source=self.recrutement,
            date_effet=self.date_effet,
            evenement=self.evenement,
        )

    def _create_affectation(self):
        """
        Crée la première affectation.
        """

        return creer_affectation(
            agent=self.agent,
            source=self.recrutement,
            evenement=self.evenement,
        )

    def _create_occupation(self):
        """
        Crée la première occupation de poste
        lorsque le recrutement comporte un poste.
        """

        if not self.recrutement.poste:
            return None

        return creer_occupation(
            agent=self.agent,
            source=self.recrutement,
            evenement=self.evenement,
        )


HandlerRegistry.register(
    "RECRUTEMENT",
    RecrutementHandler,
)