"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/conge_maladie.py

Description :
    Creator du congé de maladie.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.conge_maladie import (
    CongeMaladie,
)

from apps.rh.services.creation.base import (
    BaseEvenementCreator,
)

from apps.rh.services.creation.registry import (
    CreationRegistry,
)


class CongeMaladieCreator(
    BaseEvenementCreator,
):
    """
    Creator du congé de maladie.
    """

    model = CongeMaladie

    key = "conge_maladie"

    def process(self):
        """
        Crée la fiche spécialisée
        du congé de maladie.
        """

        data = self.payload["conge_maladie"]

        CongeMaladie.objects.create(

            evenement=self.evenement,

            debut_conge=data[
                "debut_conge"
            ],

            fin_conge=data[
                "fin_conge"
            ],

            observation=data.get(
                "observation",
                "",
            ),
        )


CreationRegistry.register(
    "CONGE_MALADIE",
    CongeMaladieCreator,
)