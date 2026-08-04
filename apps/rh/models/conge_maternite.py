# apps/rh/models/conge_maternite.py

from django.db import models
from apps.rh.models.base_evenement import BaseEvenementModel


class CongeMaternite(BaseEvenementModel):
    """
    Informations spécifiques au congé de maternité.

    Ce modèle complète un événement de carrière
    de type CONGE_MATERNITE.

    Les informations communes (agent, acte
    administratif, documents, validation, audit...)
    sont portées par EvenementCarriere.
    """

    date_debut = models.DateField(
        verbose_name="Date de début",
        help_text="Premier jour du congé de maternité.",
    )

    date_fin = models.DateField(
        verbose_name="Date de fin",
        help_text="Dernier jour du congé de maternité.",
    )

    class Meta:
        db_table = "rh_conge_maternite"

        verbose_name = "Congé de maternité"
        verbose_name_plural = "Congés de maternité"

        ordering = [
            "-date_debut",
        ]

        constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    date_fin__gte=models.F("date_debut")
                ),
                name="ck_conge_maternite_dates_coherentes",
            ),
        ]

        indexes = [
            models.Index(fields=["date_debut"]),
        ]

    def __str__(self):
        return (
            f"{self.agent} "
            f"({self.date_debut:%d/%m/%Y} - "
            f"{self.date_fin:%d/%m/%Y})"
        )

    @property
    def nombre_jours(self):
        """
        Nombre de jours du congé.

        Les dates de début et de fin sont incluses.
        """
        return (
            (self.date_fin - self.date_debut).days
            + 1
        )