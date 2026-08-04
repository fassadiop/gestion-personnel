from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Structure,
    UniteOrganisationnelle,
)


class Detachement(BaseStructureModel):
    """
    Détachement.

    Correspond au détachement temporaire d'un
    agent auprès d'une autre administration
    ou organisme.

    Cet événement modifie la position
    administrative de l'agent.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="detachement",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé.",
    )

    organisme_accueil = models.CharField(
        max_length=255,
        verbose_name="Organisme d'accueil",
        help_text="Administration ou organisme d'accueil.",
        null=True,
        blank=True,
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="detachements",
        null=True,
        blank=True,
        verbose_name="Structure d'accueil",
        help_text="Structure d'accueil si elle est gérée dans le SGCP.",
    )

    unite = models.ForeignKey(
        UniteOrganisationnelle,
        on_delete=models.PROTECT,
        related_name="detachements",
        null=True,
        blank=True,
        verbose_name="Unité organisationnelle",
        help_text="Unité organisationnelle d'accueil.",
    )

    date_debut = models.DateField(
        verbose_name="Date de début",
        help_text="Date de début du détachement.",
    )

    date_fin = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de fin",
        help_text="Date de fin prévue du détachement.",
    )

    class Meta:
        db_table = "rh_detachement"

        verbose_name = "Détachement"
        verbose_name_plural = "Détachements"

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
                name="ck_detachement_dates",
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