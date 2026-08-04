"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/nomination.py

Description :
    Handler de nomination.

Auteur : SGCP
Version : 3.0
==========================================================
"""

from apps.rh.models import (
    Affectation as AffectationEvenement,
)

from apps.rh.models.nomination import (
    Nomination,
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
    creer_occupation,
)


class NominationHandler(
    BaseAffectationHandler,
):
    """
    Handler de nomination.

    Une nomination peut entraîner :

        - un changement de poste ;

        - un changement d'unité ;

        - un changement de structure.

    Conséquences métier :

        - clôture de l'affectation courante ;

        - activation de la nouvelle affectation ;

        - clôture de l'occupation courante ;

        - création de la nouvelle occupation.

    La situation administrative reste inchangée.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.nomination = (
            self.get_evenement_data(
                "nomination",
                Nomination,
            )
        )

        self.affectation_evenement = (
            self.get_evenement_data(
                "affectation",
                AffectationEvenement,
            )
        )

        if self.nomination.structure is None:
            raise EvenementInvalideError(
                "La structure est obligatoire."
            )

        if self.nomination.poste is None:
            raise EvenementInvalideError(
                "Le poste est obligatoire."
            )

    def activate_affectation(self):
        """
        Rend effective l'affectation
        préparée lors de la création
        de l'événement.
        """

        self.affectation_evenement.est_courante = True

        self.affectation_evenement.save(
            update_fields=[
                "est_courante",
                "updated_at",
            ]
        )

        return self.affectation_evenement

    def create_occupation(self):
        """
        Crée la nouvelle occupation.
        """

        return creer_occupation(

            agent=self.agent,

            poste=self.nomination.poste,

            evenement=self.evenement,

            date_debut=self.date_effet,

            est_interim=False,
        )

    def process(self):
        """
        Exécute la nomination.
        """

        affectation = (
            self.update_affectation()
        )

        occupation = (
            self.update_occupation()
        )

        return {
            "evenement": self.evenement,
            "affectation": affectation,
            "occupation": occupation,
        }


HandlerRegistry.register(
    "NOMINATION",
    NominationHandler,
)