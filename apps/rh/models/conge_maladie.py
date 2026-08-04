# apps/rh/models/conge_maladie.py

from django.db import models

from apps.rh.models.base_evenement import BaseEvenementModel
from apps.rh.models.evenement import EvenementCarriere


class CongeMaladie(BaseEvenementModel):
    """
    Informations spécifiques à un congé de maladie.

    Ce modèle complète un événement de carrière de type
    CONGE_MALADIE.

    Il ne contient que les informations propres au congé.
    Toutes les informations communes (agent, acte administratif,
    documents, validation, audit...) sont portées par
    EvenementCarriere.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.PROTECT,
        related_name="conge_maladie",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé au congé de maladie.",
    )

    debut_conge = models.DateField(
        verbose_name="Début du congé",
        help_text="Date de début du congé de maladie.",
    )

    fin_conge = models.DateField(
        verbose_name="Fin du congé",
        help_text="Date de fin du congé de maladie.",
    )

    class Meta:
        db_table = "rh_conge_maladie"

        verbose_name = "Congé de maladie"
        verbose_name_plural = "Congés de maladie"

        ordering = [
            "-debut_conge",
            "-id",
        ]

        constraints = [
            models.CheckConstraint(
                check=models.Q(fin_conge__gte=models.F("debut_conge")),
                name="ck_conge_maladie_dates",
            ),
        ]

        indexes = [
            models.Index(fields=["evenement"]),
            models.Index(fields=["debut_conge"]),
            models.Index(fields=["fin_conge"]),
        ]

    def __str__(self):
        return (
            f"Congé maladie "
            f"du {self.debut_conge:%d/%m/%Y} "
            f"au {self.fin_conge:%d/%m/%Y}"
        )

    @property
    def nombre_jours(self):
        if not self.debut_conge or not self.fin_conge:
            return 0

        return (self.fin_conge - self.debut_conge).days + 1