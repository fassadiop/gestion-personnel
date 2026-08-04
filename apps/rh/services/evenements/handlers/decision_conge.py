"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/decision_conge.py

Description :
    Handler de décision de congé.

Auteur : SGCP
Version : 1.1
==========================================================
"""

from apps.rh.models import (
    DecisionConge,
    TypeMouvementConge,
)

from apps.rh.services.creation.utils import (
    creer_compteur_conge,
    creer_mouvement_compteur_conge,
)

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)


class DecisionCongeHandler(
    BaseEvenementHandler,
):
    """
    Handler de décision de congé.

    La validation d'une décision de congé :

        - crée le compteur de congé ;

        - crée le mouvement d'ouverture
          des droits.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.decision_conge = (
            self.get_evenement_data(
                "decision_conge",
                DecisionConge,
            )
        )

        self.type_mouvement_ouverture = (
            TypeMouvementConge.objects.get(
                code="OUVERTURE"
            )
        )

    def process(self):
        """
        Exécute la validation de la décision
        de congé.
        """

        compteur = (
            creer_compteur_conge(
                decision_conge=(
                    self.decision_conge
                ),
            )
        )

        mouvement = (
            creer_mouvement_compteur_conge(

                compteur=compteur,

                type_mouvement=(
                    self.type_mouvement_ouverture
                ),

                nombre_jours=(
                    self.decision_conge
                    .nombre_jours_accordes
                ),

                date_mouvement=(
                    self.evenement.date_effet
                ),

                observation=(
                    "Ouverture des droits "
                    "à congé."
                ),
            )
        )

        return {

            "evenement": self.evenement,

            "decision_conge": (
                self.decision_conge
            ),

            "compteur": compteur,

            "mouvement": mouvement,

        }


HandlerRegistry.register(
    "DECISION_CONGE",
    DecisionCongeHandler,
)