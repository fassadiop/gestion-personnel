# apps/rh/models/reclassement.py

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere

from apps.rh.models.referentiels import (
    Corps,
    Grade,
    Classe,
    Echelon,
)


class Reclassement(BaseStructureModel):
    """
    Informations spécifiques à un reclassement.

    Un reclassement entraîne une évolution
    de la situation administrative de l'agent.

    Les anciennes informations sont déjà
    historisées dans SituationAdministrative.

    Ce modèle ne contient donc que les
    nouvelles valeurs.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="reclassement",
        verbose_name="Événement de carrière",
        help_text="Événement de reclassement.",
    )

    corps = models.ForeignKey(
        Corps,
        on_delete=models.PROTECT,
        related_name="reclassements",
        verbose_name="Nouveau corps",
        null=True,
        blank=True,
    )

    grade = models.ForeignKey(
        Grade,
        on_delete=models.PROTECT,
        related_name="reclassements",
        verbose_name="Nouveau grade",
        null=True,
        blank=True,
    )

    classe = models.ForeignKey(
        Classe,
        on_delete=models.PROTECT,
        related_name="reclassements",
        verbose_name="Nouvelle classe",
        null=True,
        blank=True,
    )

    echelon = models.ForeignKey(
        Echelon,
        on_delete=models.PROTECT,
        related_name="reclassements",
        verbose_name="Nouvel échelon",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "rh_reclassement"

        verbose_name = "Reclassement"
        verbose_name_plural = "Reclassements"

        ordering = [
            "-id",
        ]

        indexes = [

            models.Index(fields=["grade"]),

            models.Index(fields=["classe"]),

            models.Index(fields=["echelon"]),

        ]

    def __str__(self):
        return (
            f"Reclassement de {self.evenement.agent}"
        )