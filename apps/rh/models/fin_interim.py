from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere


class FinInterim(BaseStructureModel):
    """
    Fin d'intérim.

    Correspond à la fin d'une occupation
    temporaire de poste.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="fin_interim",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé.",
    )

    date_fin_interim = models.DateField(
        verbose_name="Date de fin d'intérim",
        help_text="Date effective de fin d'intérim.",
    )

    class Meta:
        db_table = "rh_fin_interim"

        verbose_name = "Fin d'intérim"
        verbose_name_plural = "Fins d'intérim"

        ordering = (
            "-date_fin_interim",
            "-id",
        )

        indexes = (
            models.Index(fields=("evenement",)),
            models.Index(fields=("date_fin_interim",)),
        )

    def __str__(self):
        return (
            f"{self.evenement.agent} - "
            f"{self.date_fin_interim:%d/%m/%Y}"
        )