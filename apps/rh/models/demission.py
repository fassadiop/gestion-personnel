# apps/rh/models/demission.py

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere


class Demission(BaseStructureModel):
    """
    Démission.

    Correspond à la démission définitive
    d'un agent de la Fonction publique.

    Cet événement met fin définitivement
    à la carrière de l'agent.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="demission",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé.",
    )

    motif = models.TextField(
        blank=True,
        default="",
        verbose_name="Motif",
        help_text="Motif de la démission.",
    )

    class Meta:
        db_table = "rh_demission"

        verbose_name = "Démission"
        verbose_name_plural = "Démissions"

        ordering = (
            "-id",
        )

        indexes = (
            models.Index(
                fields=("evenement",),
            ),
        )

    def __str__(self):
        return f"{self.evenement.agent}"