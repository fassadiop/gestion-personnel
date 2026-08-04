"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/creators/recrutement.py

Description :
    Creator de l'événement Recrutement.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.referentiels import PositionAdministrative
from apps.rh.services.creation.base import (
    BaseEvenementCreator,
)

from apps.rh.services.creation.exceptions import (
    DonneesEvenementInvalidesError,
)

from apps.rh.services.creation.registry import (
    CreationRegistry,
)

from apps.rh.services.creation.utils import (
    creer_recrutement,
)


class RecrutementCreator(
    BaseEvenementCreator,
):
    """
    Creator de l'événement Recrutement.

    Responsabilités :

        - créer l'événement de carrière ;

        - créer la fiche spécialisée
          de recrutement.

    Les conséquences sur la carrière
    seront produites uniquement lors
    de la validation de l'événement
    par le moteur de carrière.
    """

    # =====================================================
    # Chargement des données
    # =====================================================

    def load_data(self):
        """
        Charge les données spécialisées.
        """

        self.recrutement = (
            self.payload.get(
                "recrutement"
            )
        )

    # =====================================================
    # Validation
    # =====================================================

    def validate(self):
        """
        Validation spécifique.
        """

        super().validate()

        if self.recrutement is None:
            raise DonneesEvenementInvalidesError(
                "Les informations du recrutement "
                "sont obligatoires."
            )

        champs_obligatoires = [

            "corps",

            "grade",

            "classe",

            "echelon",

            "structure",

            "date_recrutement",

        ]

        for champ in champs_obligatoires:

            if self.recrutement.get(champ) is None:

                raise DonneesEvenementInvalidesError(
                    f"Le champ '{champ}' est obligatoire."
                )

    # =====================================================
    # Traitement
    # =====================================================

    def process(self):
        """
        Crée la fiche spécialisée
        de recrutement.
        """

        position = PositionAdministrative.objects.get(
            code="EN_ACTIVITE"
        )

        self.evenement.position_administrative = position
        self.evenement.save(update_fields=["position_administrative"])

        creer_recrutement(

            evenement=self.evenement,

            corps=self.recrutement["corps"],

            grade=self.recrutement["grade"],

            classe=self.recrutement["classe"],

            echelon=self.recrutement["echelon"],

            structure=self.recrutement["structure"],

            date_recrutement=self.recrutement[
                "date_recrutement"
            ],
        )


CreationRegistry.register(
    "RECRUTEMENT",
    RecrutementCreator,
)