from django.db import models
from apps.rh.core.base import BaseStructureModel
from apps.rh.models.agent import Agent
from apps.rh.models.organisation import Poste, Structure, UniteOrganisationnelle


class Affectation(BaseStructureModel):
    """
    Historique des affectations d'un agent.
    """

    evenement = models.OneToOneField(
        "EvenementCarriere",
        on_delete=models.CASCADE,
        related_name="affectation",
        verbose_name="Événement de carrière",
    )

    agent = models.ForeignKey(
        Agent,
        on_delete=models.PROTECT,
        related_name="affectations",
        verbose_name="Agent",
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="affectations",
        verbose_name="Structure",
    )

    unite = models.ForeignKey(
        UniteOrganisationnelle,
        on_delete=models.PROTECT,
        related_name="affectations",
        verbose_name="Unité organisationnelle",
        null=True,
        blank=True,
    )

    poste = models.ForeignKey(
        Poste,
        on_delete=models.PROTECT,
        related_name="affectations",
        verbose_name="Poste",
        null=True,
        blank=True,
    )

    est_courante = models.BooleanField(
        default=False,
        verbose_name="Affectation courante",
    )

    class Meta:
        db_table = "rh_affectation"
        verbose_name = "Affectation"
        verbose_name_plural = "Affectations"

        indexes = [
            models.Index(fields=["agent"]),
            models.Index(fields=["structure"]),
            models.Index(fields=["unite"]),
            models.Index(fields=["poste"]),
            models.Index(fields=["est_courante"]),
        ]

    def __str__(self):
        return (
            f"{self.agent} → "
            f"{self.structure} / "
            f"{self.unite}"
        )