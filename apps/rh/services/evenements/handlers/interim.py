"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/interim.py

Description :
    Handler d'intérim.

Auteur : SGCP
Version : 3.0
==========================================================
"""

from apps.rh.models.interim import Interim

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.exceptions import (
    AffectationError,
    EvenementInvalideError,
    OccupationPosteError,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)

from apps.rh.services.evenements.utils import (
    creer_occupation,
    get_affectation_courante,
    get_interim_actif,
    get_occupation_active,
)


class InterimHandler(BaseEvenementHandler):
    """
    Handler d'intérim.

    Conséquences métier :

        - création d'une occupation
          temporaire ;

        - aucune modification de
          l'affectation ;

        - aucune modification de
          la situation administrative ;

        - aucune modification de
          l'occupation principale.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.interim = self.get_evenement_data(
            "interim",
            Interim,
        )

        if self.evenement.date_fin is None:
            raise EvenementInvalideError(
                "Un intérim doit obligatoirement comporter une date de fin."
            )

        affectation = get_affectation_courante(self.agent)

        if affectation is None:
            raise AffectationError(
                "L'agent ne possède aucune affectation en cours."
            )

        self.interim_actif = get_interim_actif(
            self.agent
        )

        if self.interim_actif is not None:
            raise OccupationPosteError(
                "L'agent assure déjà un intérim en cours."
            )

        self.occupation_active = get_occupation_active(
            self.interim.poste
        )

        if self.occupation_active is None:
            return

        if self.occupation_active.agent == self.agent:
            raise OccupationPosteError(
                "Un agent ne peut pas assurer l'intérim de son propre poste."
            )

        if self.occupation_active.est_interim:
            raise OccupationPosteError(
                "Ce poste fait déjà l'objet d'un intérim."
            )

    def process(self):
        """
        Exécute l'intérim.
        """

        occupation = creer_occupation(

            agent=self.agent,

            poste=self.interim.poste,

            evenement=self.evenement,

            date_debut=self.date_effet,

            date_fin=self.evenement.date_fin,

            est_interim=True,

        )

        return {
            "evenement": self.evenement,
            "occupation": occupation,
        }


HandlerRegistry.register(
    "INTERIM",
    InterimHandler,
)