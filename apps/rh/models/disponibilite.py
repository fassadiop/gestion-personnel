from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere


class Disponibilite(BaseStructureModel):
    """
    Disponibilité.

    Correspond au placement temporaire d'un
    agent en position de disponibilité.

    Cet événement modifie la position
    administrative de l'agent.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="disponibilite",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé.",
    )

    motif = models.CharField(
        max_length=255,
        verbose_name="Motif",
        help_text="Motif de la disponibilité.",
    )

    date_debut = models.DateField(
        verbose_name="Date de début",
        help_text="Date de début de la disponibilité.",
    )

    date_fin = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de fin",
        help_text="Date de fin prévue.",
    )

    class Meta:
        db_table = "rh_disponibilite"

        verbose_name = "Disponibilité"
        verbose_name_plural = "Disponibilités"

        ordering = (
            "-date_debut",
            "-id",
        )

        constraints = (
            models.CheckConstraint(
                condition=(
                    models.Q(date_fin__isnull=True)
                    |
                    models.Q(
                        date_fin__gte=models.F("date_debut")
                    )
                ),
                name="ck_disponibilite_dates",
            ),
        )

        indexes = (
            models.Index(fields=("evenement",)),
            models.Index(fields=("date_debut",)),
            models.Index(fields=("date_fin",)),
        )

    def __str__(self):
        return (
            f"{self.evenement.agent} - "
            f"{self.date_debut:%d/%m/%Y}"
        )