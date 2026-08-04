# apps/rh/models/prise_service_initiale.py

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Structure,
    UniteOrganisationnelle,
)


class PriseServiceInitiale(BaseStructureModel):
    """
    Prise de service initiale.

    Correspond à l'arrivée effective d'un agent
    dans son ministère après son recrutement.

    Cet événement crée la première affectation
    de l'agent.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="prise_service_initiale",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé.",
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="prises_service_initiales",
        verbose_name="Structure",
        help_text="Structure de prise de service.",
    )

    unite = models.ForeignKey(
        UniteOrganisationnelle,
        on_delete=models.PROTECT,
        related_name="prises_service_initiales",
        null=True,
        blank=True,
        verbose_name="Unité organisationnelle",
        help_text="Unité organisationnelle d'affectation.",
    )

    date_prise_service = models.DateField(
        verbose_name="Date de prise de service",
        help_text="Date effective de prise de service.",
    )

    class Meta:
        db_table = "rh_prise_service_initiale"

        verbose_name = "Prise de service initiale"
        verbose_name_plural = (
            "Prises de service initiales"
        )

        ordering = (
            "-date_prise_service",
            "-id",
        )

        constraints = (
            models.UniqueConstraint(
                fields=("evenement",),
                name="uq_prise_service_initiale_evenement",
            ),
        )

        indexes = (
            models.Index(fields=("evenement",)),
            models.Index(fields=("structure",)),
            models.Index(fields=("unite",)),
            models.Index(fields=("date_prise_service",)),
        )

    def __str__(self):
        return (
            f"{self.evenement.agent} - "
            f"{self.date_prise_service:%d/%m/%Y}"
        )