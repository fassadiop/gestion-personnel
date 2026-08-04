"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/absence.py

Description :
    Handler de l'autorisation d'absence.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Absence,
)

from apps.rh.models.referentiels import TypeMouvementConge
from apps.rh.services.creation.utils import creer_mouvement_compteur_conge
from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.exceptions import EvenementInvalideError
from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)


class AbsenceHandler(
    BaseEvenementHandler,
):
    """
    Handler de l'autorisation d'absence.

    Cette première version valide
    uniquement l'existence de la fiche
    spécialisée.

    Les traitements liés à la déduction
    automatique du reliquat de congé
    seront implémentés dans une version
    ultérieure.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.absence = (
            self.get_evenement_data(
                "absence",
                Absence,
            )
        )

        self.type_mouvement_absence = (
            TypeMouvementConge.objects.get(
                code="ABSENCE"
            )
        )

    def process(self):
        """
        Exécute le traitement métier
        de l'absence.
        """

        # Aucun jour à déduire.
        if self.absence.jours_deductibles == 0:

            return {

                "evenement": self.evenement,

                "absence": self.absence,

            }

        compteur = self.agent.compteur_conge_actif

        if compteur is None:

            raise EvenementInvalideError(
                "Aucun compteur de congé disponible "
                "pour cet agent."
            )

        if (
            self.absence.jours_deductibles
            > compteur.reliquat
        ):

            raise EvenementInvalideError(
                "Le reliquat du compteur de congé "
                "est insuffisant."
            )

        creer_mouvement_compteur_conge(
            compteur=compteur,
            type_mouvement=self.type_mouvement_absence,
            nombre_jours=self.absence.jours_deductibles,
            date_mouvement=self.evenement.date_effet,
            observation=(
                "Déduction suite à une "
                "autorisation d'absence."
            ),
        )

        return {

            "evenement": self.evenement,

            "absence": self.absence,

            "compteur": compteur,

        }


HandlerRegistry.register(
    "ABSENCE",
    AbsenceHandler,
)