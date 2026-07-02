# apps/rh/models/titularisation.py

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere

from apps.rh.models.referentiels import (
    Grade,
    Classe,
    Echelon,
    PositionAdministrative,
)


class Titularisation(BaseStructureModel):
    """
    Informations spécifiques à une titularisation.

    Une titularisation confirme définitivement
    un agent dans son corps.

    Elle entraîne la création d'une nouvelle
    SituationAdministrative.

    Les anciennes informations sont déjà
    historisées dans SituationAdministrative.

    Ce modèle ne contient que les nouvelles
    valeurs.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="titularisation",
        verbose_name="Événement de carrière",
        help_text="Événement de titularisation.",
    )

    position_administrative = models.ForeignKey(
        PositionAdministrative,
        on_delete=models.PROTECT,
        related_name="titularisations",
        verbose_name="Nouvelle position administrative",
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.PROTECT,
        related_name="titularisations",
        verbose_name="Grade",
    )

    classe = models.ForeignKey(
        Classe,
        on_delete=models.PROTECT,
        related_name="titularisations",
        verbose_name="Classe",
    )

    echelon = models.ForeignKey(
        Echelon,
        on_delete=models.PROTECT,
        related_name="titularisations",
        verbose_name="Échelon",
    )

    class Meta:
        db_table = "rh_titularisation"

        verbose_name = "Titularisation"
        verbose_name_plural = "Titularisations"

        ordering = [
            "-id",
        ]

        indexes = [

            models.Index(fields=["position_administrative"]),

            models.Index(fields=["grade"]),

            models.Index(fields=["classe"]),

            models.Index(fields=["echelon"]),

        ]

    def __str__(self):
        return (
            f"Titularisation de {self.evenement.agent}"
        )