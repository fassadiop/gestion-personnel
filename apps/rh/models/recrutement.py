# apps/rh/models/recrutement.py

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Structure,
)

from apps.rh.models.referentiels import (
    Corps,
    Grade,
    Classe,
    Echelon,
)


class Recrutement(BaseStructureModel):
    """
    Informations spécifiques à un recrutement.

    Ce modèle complète un événement de carrière de type
    RECRUTEMENT.

    Il contient les informations nécessaires à la création
    de la première SituationAdministrative de l'agent.
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

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="recrutements",
        verbose_name="Structure",
    )

    date_recrutement = models.DateField(
        verbose_name="Date de recrutement",
        help_text="Date effective du recrutement dans la fonction publique.",
    )

    numero_document = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Numéro du document",
        help_text="Numéro officiel du document.",
    )

    class Meta:
        db_table = "rh_recrutement"

        verbose_name = "Recrutement"
        verbose_name_plural = "Recrutements"

        ordering = [
            "-date_recrutement",
            "-id",
        ]

        indexes = [

            models.Index(fields=["date_recrutement"]),

            models.Index(fields=["structure"]),

        ]

    def __str__(self):
        return (
            f"Recrutement de {self.evenement.agent}"
        )