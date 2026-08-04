from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere


class Reintegration(BaseStructureModel):
    """
    Réintégration.

    Correspond à la réintégration d'un agent
    après une formation, une mise à disposition, un détachement
    ou une disponibilité.

    Cet événement modifie la position
    administrative de l'agent.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="reintegration",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé.",
    )

    motif = models.CharField(
        max_length=255,
        verbose_name="Motif",
        help_text="Motif de la réintégration.",
    )

    date_reintegration = models.DateField(
        verbose_name="Date de réintégration",
        help_text="Date effective de réintégration.",
    )

    class Meta:
        db_table = "rh_reintegration"

        verbose_name = "Réintégration"
        verbose_name_plural = "Réintégrations"

        ordering = (
            "-date_reintegration",
            "-id",
        )

        indexes = (
            models.Index(fields=("evenement",)),
            models.Index(fields=("date_reintegration",)),
        )

    def __str__(self):
        return (
            f"{self.evenement.agent} - "
            f"{self.date_reintegration:%d/%m/%Y}"
        )