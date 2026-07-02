# apps/rh/models/detachement.py

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Structure,
    UniteOrganisationnelle,
    Poste,
)
from apps.rh.models.referentiels import PositionAdministrative


class Detachement(BaseStructureModel):
    """
    Informations spécifiques à un détachement.

    Le détachement place temporairement un agent
    dans une autre position administrative.

    Il peut être accompagné d'une nouvelle
    affectation dans une structure d'accueil.

    Ce modèle ne contient que les informations
    de destination.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="detachement",
        verbose_name="Événement de carrière",
        help_text="Événement de détachement.",
    )

    position_administrative = models.ForeignKey(
        PositionAdministrative,
        on_delete=models.PROTECT,
        related_name="detachements",
        verbose_name="Position administrative",
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="detachements",
        verbose_name="Structure d'accueil",
    )

    unite = models.ForeignKey(
        UniteOrganisationnelle,
        on_delete=models.PROTECT,
        related_name="detachements",
        verbose_name="Unité d'accueil",
        null=True,
        blank=True,
    )

    poste = models.ForeignKey(
        Poste,
        on_delete=models.PROTECT,
        related_name="detachements",
        verbose_name="Poste occupé",
        null=True,
        blank=True,
    )

    date_debut = models.DateField(
        verbose_name="Date de début",
        help_text="Date de prise d'effet du détachement.",
    )

    date_fin_prevue = models.DateField(
        verbose_name="Date de fin prévisionnelle",
        help_text="Date prévue de fin du détachement.",
    )

    class Meta:
        db_table = "rh_detachement"

        verbose_name = "Détachement"
        verbose_name_plural = "Détachements"

        ordering = [
            "-date_debut",
            "-id",
        ]

        constraints = [

            models.CheckConstraint(
                condition=models.Q(
                    date_fin_prevue__gte=models.F("date_debut")
                ),
                name="ck_detachement_dates",
            ),

        ]

        indexes = [

            models.Index(fields=["position_administrative"]),

            models.Index(fields=["structure"]),

            models.Index(fields=["poste"]),

            models.Index(fields=["date_debut"]),

            models.Index(fields=["date_fin_prevue"]),

        ]

    def __str__(self):
        return (
            f"Détachement de {self.evenement.agent}"
        )