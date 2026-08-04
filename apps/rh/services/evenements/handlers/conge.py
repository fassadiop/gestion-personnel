"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/handlers/conge.py

Description :
    Handler de consommation d'un congé.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Conge,
    TypeMouvementConge,
)

from apps.rh.services.creation.utils import (
    creer_mouvement_compteur_conge,
)

from apps.rh.services.evenements.base import (
    BaseEvenementHandler,
)

from apps.rh.services.evenements.registry import (
    HandlerRegistry,
)


class CongeHandler(
    BaseEvenementHandler,
):
    """
    Handler du congé.

    La validation d'un congé :

        - vérifie le reliquat ;

        - crée un mouvement
          de consommation.
    """

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        self.conge = (
            self.get_evenement_data(
                "conge",
                Conge,
            )
        )

        self.compteur = (
            self.conge
            .decision_conge
            .compteur
        )

        self.type_mouvement = (
            TypeMouvementConge.objects.get(
                code="CONSOMMATION"
            )
        )

        if (
            self.conge.nombre_jours
            > self.compteur.reliquat
        ):
            raise ValueError(
                "Le reliquat de congé est insuffisant."
            )

    def process(self):
        """
        Exécute la consommation
        du compteur.
        """

        mouvement = (
            creer_mouvement_compteur_conge(

                compteur=self.compteur,

                type_mouvement=(
                    self.type_mouvement
                ),

                nombre_jours=(
                    self.conge.nombre_jours
                ),

                date_mouvement=(
                    self.evenement.date_effet
                ),

                observation=(
                    "Consommation d'un congé."
                ),
            )
        )

        return {

            "evenement": self.evenement,

            "conge": self.conge,

            "compteur": self.compteur,

            "mouvement": mouvement,

        }


HandlerRegistry.register(
    "CONGE",
    CongeHandler,
)