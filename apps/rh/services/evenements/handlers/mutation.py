"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/mutation.py

Description :
    Handler de mutation.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.mutation import Mutation

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


class MutationHandler(BaseAffectationHandler):
    """
    Handler de mutation.

    Une mutation entraîne un changement
    d'affectation de l'agent.

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
        Validation spécifique à la mutation.
        """

        super().validate()

        self.mutation = self.load_evenement_data(
            "mutation",
            Mutation,
        )

        if not self.mutation.structure:
            raise EvenementInvalideError(
                "La structure de destination est obligatoire."
            )

        if not self.mutation.unite:
            raise EvenementInvalideError(
                "L'unité organisationnelle de destination est obligatoire."
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
            source=self.mutation,
            evenement=self.evenement,
        )

    # =====================================================
    # Création de la nouvelle occupation
    # =====================================================

    def create_new_occupation(self):
        """
        Crée la nouvelle occupation de poste.

        Retourne None lorsqu'aucun poste
        n'est concerné.
        """

        if not self.mutation.poste:
            return None

        return creer_occupation(
            agent=self.agent,
            source=self.mutation,
            evenement=self.evenement,
        )


HandlerRegistry.register(
    "MUTATION",
    MutationHandler,
)