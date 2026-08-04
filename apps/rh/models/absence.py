# apps/rh/models/absence.py

from django.db import models

from apps.rh.models.base_evenement import BaseEvenementModel
from apps.rh.models.referentiels import TypeAbsence


class Absence(BaseEvenementModel):
    """
    Autorisation d'absence accordée à un agent.

    Une absence est un événement administratif autorisant
    un agent à s'absenter du service pendant une période
    déterminée.

    Les informations communes (agent, acte administratif,
    signataire, dates, etc.) sont portées par
    EvenementCarriere.
    """

    type_absence = models.ForeignKey(
        TypeAbsence,
        on_delete=models.PROTECT,
        related_name="absences",
        verbose_name="Type d'absence",
        help_text="Nature de l'absence.",
    )

    date_debut = models.DateField(
        verbose_name="Date de début",
        help_text="Premier jour d'absence.",
    )

    date_fin = models.DateField(
        verbose_name="Date de fin",
        help_text="Dernier jour d'absence autorisé.",
    )

    jours_deductibles = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Jours déductibles",
        help_text=(
            "Nombre de jours imputables sur le "
            "compteur de congé conformément à "
            "l'autorisation d'absence."
        ),
    )

    motif = models.TextField(
        blank=True,
        default="",
        verbose_name="Motif",
        help_text="Motif de l'autorisation d'absence.",
    )

    class Meta:
        db_table = "rh_absence"

        verbose_name = "Autorisation d'absence"
        verbose_name_plural = "Autorisations d'absence"

        ordering = [
            "-date_debut",
        ]

        constraints = [

            models.CheckConstraint(
                condition=models.Q(
                    date_fin__gte=models.F("date_debut")
                ),
                name="ck_absence_dates_coherentes",
            ),

        ]

        indexes = [

            models.Index(fields=["type_absence"]),

            models.Index(fields=["date_debut"]),

        ]

    def __str__(self):
        return (
            f"{self.agent} "
            f"({self.date_debut:%d/%m/%Y} - "
            f"{self.date_fin:%d/%m/%Y})"
        )

    # ==========================================================
    # PROPRIÉTÉS MÉTIER
    # ==========================================================

    @property
    def nombre_jours(self):
        """
        Nombre de jours d'absence.

        La date de début et la date de fin
        sont toutes les deux incluses.
        """
        return (
            (self.date_fin - self.date_debut).days
            + 1
        )