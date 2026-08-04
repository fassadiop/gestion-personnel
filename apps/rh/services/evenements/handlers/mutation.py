"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/mutation.py

Description :
    Handler de mutation.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from apps.rh.models.mutation import (
    Mutation,
)

from apps.rh.services.evenements.handlers.base_affectation import (
    BaseAffectationHandler,
)

from apps.rh.services.evenements.exceptions import (
    EvenementInvalideError,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    creer_affectation,
)


class MutationHandler(
    BaseAffectationHandler,
):
    """
    Handler de mutation.

    Conséquences métier :

        - clôture de l'affectation courante ;

        - création d'une nouvelle affectation.

    La situation administrative et
    l'occupation de poste restent inchangées.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.mutation = (
            self.get_evenement_data(
                "mutation",
                Mutation,
            )
        )

        if self.mutation.structure is None:
            raise EvenementInvalideError(
                "La structure de destination est obligatoire."
            )

    def create_affectation(self):
        """
        Crée la nouvelle affectation.
        """

        return creer_affectation(

            agent=self.agent,

            source=self.mutation,

            evenement=self.evenement,

        )

    def process(self):
        """
        Exécute la mutation.
        """

        affectation = (
            self.update_affectation()
        )

        return {
            "evenement": self.evenement,
            "affectation": affectation,
        }


HandlerRegistry.register(
    "MUTATION",
    MutationHandler,
)