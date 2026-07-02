# apps/rh/models/recrutement.py

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Structure,
    UniteOrganisationnelle,
    Poste,
)

from apps.rh.models.referentiels import (
    Corps,
    Grade,
    Classe,
    Echelon,
    PositionAdministrative,
)


class Recrutement(BaseStructureModel):
    """
    Informations spécifiques à un recrutement.

    Ce modèle complète un événement de carrière de type
    RECRUTEMENT.

    Il contient les informations nécessaires à la création
    de la première :

        - SituationAdministrative
        - Affectation
        - OccupationPoste
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="recrutement",
        verbose_name="Événement de carrière",
        help_text="Événement de recrutement.",
    )

    corps = models.ForeignKey(
        Corps,
        on_delete=models.PROTECT,
        related_name="recrutements",
        verbose_name="Corps",
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.PROTECT,
        related_name="recrutements",
        verbose_name="Grade",
    )

    classe = models.ForeignKey(
        Classe,
        on_delete=models.PROTECT,
        related_name="recrutements",
        verbose_name="Classe",
    )

    echelon = models.ForeignKey(
        Echelon,
        on_delete=models.PROTECT,
        related_name="recrutements",
        verbose_name="Échelon",
    )

    position_administrative = models.ForeignKey(
        PositionAdministrative,
        on_delete=models.PROTECT,
        related_name="recrutements",
        verbose_name="Position administrative",
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="recrutements",
        verbose_name="Structure",
    )

    unite = models.ForeignKey(
        UniteOrganisationnelle,
        on_delete=models.PROTECT,
        related_name="recrutements",
        verbose_name="Unité organisationnelle",
        null=True,
        blank=True,
    )

    poste = models.ForeignKey(
        Poste,
        on_delete=models.PROTECT,
        related_name="recrutements",
        verbose_name="Poste",
        null=True,
        blank=True,
    )

    date_prise_service = models.DateField(
        verbose_name="Date de prise de service",
        help_text="Date effective de prise de service.",
    )

    date_anciennete = models.DateField(
        verbose_name="Date d'ancienneté",
        help_text=(
            "Date retenue pour le calcul de l'ancienneté "
            "administrative."
        ),
    )

    class Meta:
        db_table = "rh_recrutement"

        verbose_name = "Recrutement"
        verbose_name_plural = "Recrutements"

        ordering = [
            "-date_prise_service",
            "-id",
        ]

        indexes = [

            models.Index(fields=["date_prise_service"]),

            models.Index(fields=["structure"]),

            models.Index(fields=["poste"]),

        ]

    def __str__(self):
        return (
            f"Recrutement de {self.evenement.agent}"
        )