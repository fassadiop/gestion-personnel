"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/affectation.py

Description :
    Handler d'affectation.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.affectation import (
    Affectation as AffectationEvenement
)

from apps.rh.services.evenements.handlers.base_affectation import (
    BaseAffectationHandler,
)
from apps.rh.services.evenements.exceptions import (
    EvenementInvalideError,
)
from apps.rh.services.evenements.registry import HandlerRegistry
from apps.rh.services.evenements.utils import (
    creer_affectation,
    creer_occupation,
)


class AffectationHandler(BaseAffectationHandler):
    """
    Handler d'affectation.

    Une affectation modifie l'affectation administrative
    d'un agent et, le cas échéant, son occupation de poste.

    Conséquences métier :

        - clôture de l'affectation courante ;
        - clôture de l'occupation de poste courante ;
        - création d'une nouvelle affectation ;
        - création éventuelle d'une nouvelle occupation.
    """

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):
        """
        Validation spécifique à l'affectation.
        """

        super().validate()

        self.affectation = self.load_evenement_data(
            "affectation",
            AffectationEvenement,
        )

        if not self.affectation.structure:
            raise EvenementInvalideError(
                "La structure est obligatoire."
            )

        if not self.affectation.unite:
            raise EvenementInvalideError(
                "L'unité organisationnelle est obligatoire."
            )

    # =====================================================
    # Création de la nouvelle affectation
    # =====================================================

    def create_new_affectation(self):
        """
        Crée la nouvelle affectation.
        """

        return creer_affectation(
            agent=self.agent,
            source=self.affectation,
            evenement=self.evenement,
        )

    # =====================================================
    # Création de la nouvelle occupation
    # =====================================================

    def create_new_occupation(self):
        """
        Crée la nouvelle occupation de poste.

        Retourne None lorsqu'aucun poste
        n'est renseigné.
        """

        if not self.affectation.poste:
            return None

        return creer_occupation(
            agent=self.agent,
            source=self.affectation,
            evenement=self.evenement,
        )


HandlerRegistry.register(
    "AFFECTATION",
    AffectationHandler,
)