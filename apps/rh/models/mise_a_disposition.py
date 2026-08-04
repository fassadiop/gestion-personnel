# apps/rh/models/mise_a_disposition.py

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Structure,
    UniteOrganisationnelle,
)


class MiseADisposition(BaseStructureModel):
    """
    Mise à disposition.

    Correspond à la mise à disposition temporaire
    d'un agent auprès d'une autre administration,
    d'un organisme public ou d'un projet.

    Cet événement modifie la position
    administrative de l'agent.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="mise_a_disposition",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé.",
    )

    organisme_accueil = models.CharField(
        max_length=255,
        verbose_name="Organisme d'accueil",
        help_text="Administration ou organisme d'accueil.",
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="mises_a_disposition",
        null=True,
        blank=True,
        verbose_name="Structure d'accueil",
        help_text="Structure d'accueil si elle est gérée dans le SGCP.",
    )

    unite = models.ForeignKey(
        UniteOrganisationnelle,
        on_delete=models.PROTECT,
        related_name="mises_a_disposition",
        null=True,
        blank=True,
        verbose_name="Unité organisationnelle",
        help_text="Unité d'accueil si applicable.",
    )

    date_debut = models.DateField(
        verbose_name="Date de début",
        help_text="Date de début de la mise à disposition.",
    )

    date_fin = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de fin",
        help_text="Date de fin prévue de la mise à disposition.",
    )

    class Meta:
        db_table = "rh_mise_a_disposition"

        verbose_name = "Mise à disposition"
        verbose_name_plural = "Mises à disposition"

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
                name="ck_mise_a_disposition_dates",
            ),
        )

        indexes = (
            models.Index(fields=("evenement",)),
            models.Index(fields=("organisme_accueil",)),
            models.Index(fields=("structure",)),
            models.Index(fields=("unite",)),
            models.Index(fields=("date_debut",)),
            models.Index(fields=("date_fin",)),
        )

    def __str__(self):
        return (
            f"{self.evenement.agent} - "
            f"{self.organisme_accueil}"
        )