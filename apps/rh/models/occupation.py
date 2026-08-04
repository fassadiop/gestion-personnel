from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.agent import Agent
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import Poste


class OccupationPoste(BaseStructureModel):
    """
    Historique des occupations de poste.

    Une occupation est créée exclusivement
    par un événement de carrière.

    Exemples :
    
        - Affectation
        - Mutation
        - Nomination
        - Intérim
    """

    agent = models.ForeignKey(
        Agent,
        on_delete=models.PROTECT,
        related_name="occupations_poste",
        verbose_name="Agent",
    )

    poste = models.ForeignKey(
        Poste,
        on_delete=models.PROTECT,
        related_name="occupations",
        verbose_name="Poste",
    )

    evenement = models.ForeignKey(
        EvenementCarriere,
        on_delete=models.PROTECT,
        related_name="occupations_poste",
        verbose_name="Événement",
    )

    date_debut = models.DateField(
        verbose_name="Date de début",
    )

    date_fin = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de fin",
    )

    est_interim = models.BooleanField(
        default=False,
        verbose_name="Occupation d'intérim",
        help_text=(
            "Indique que cette occupation "
            "correspond à un intérim."
        ),
    )

    class Meta:

        db_table = "rh_occupation_poste"

        verbose_name = "Occupation de poste"
        verbose_name_plural = "Occupations de poste"

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
                name="ck_occupation_poste_dates",
            ),

            models.UniqueConstraint(
                fields=("poste",),
                condition=models.Q(date_fin__isnull=True),
                name="uq_poste_occupation_active",
            ),

        )

        indexes = (

            models.Index(fields=("agent",)),

            models.Index(fields=("poste",)),

            models.Index(fields=("evenement",)),

            models.Index(fields=("date_debut",)),

            models.Index(fields=("date_fin",)),

            models.Index(fields=["agent", "est_interim"]),

        )

    def __str__(self):

        return f"{self.agent} - {self.poste}"