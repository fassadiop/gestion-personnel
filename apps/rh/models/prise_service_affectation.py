from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Structure,
    UniteOrganisationnelle,
)


class PriseServiceAffectation(BaseStructureModel):
    """
    Prise de service après une affectation.

    Correspond à la prise de fonction effective
    d'un agent dans sa nouvelle structure
    d'affectation.

    Cet événement crée la nouvelle affectation
    administrative de l'agent.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="prise_service_affectation",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé.",
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="prises_service_affectation",
        verbose_name="Structure",
        help_text="Structure de prise de service.",
    )

    unite = models.ForeignKey(
        UniteOrganisationnelle,
        on_delete=models.PROTECT,
        related_name="prises_service_affectation",
        null=True,
        blank=True,
        verbose_name="Unité organisationnelle",
        help_text="Unité organisationnelle de prise de service.",
    )

    date_prise_service = models.DateField(
        verbose_name="Date de prise de service",
        help_text="Date effective de prise de service.",
    )

    class Meta:
        db_table = "rh_prise_service_affectation"

        verbose_name = "Prise de service après affectation"
        verbose_name_plural = (
            "Prises de service après affectation"
        )

        ordering = (
            "-date_prise_service",
            "-id",
        )

        constraints = (
            models.UniqueConstraint(
                fields=("evenement",),
                name="uq_ps_affectation_evenement",
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