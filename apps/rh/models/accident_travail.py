"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : models/accident_travail.py

Description :
    Modèle de l'accident de travail.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.db import models

from apps.rh.models.base_evenement import (
    BaseEvenementModel,
)


class AccidentTravail(
    BaseEvenementModel,
):
    """
    Informations spécifiques à un accident de travail.
    """

    date_accident = models.DateField(
        verbose_name="Date de l'accident",
        help_text="Date de survenance de l'accident.",
    )

    lieu_accident = models.CharField(
        max_length=255,
        verbose_name="Lieu de l'accident",
    )

    circonstances = models.TextField(
        verbose_name="Circonstances",
        help_text="Description succincte des circonstances de l'accident.",
    )

    consequences = models.TextField(
        blank=True,
        default="",
        verbose_name="Conséquences",
        help_text="Conséquences administratives constatées.",
    )

    observation = models.TextField(
        blank=True,
        default="",
        verbose_name="Observation",
    )

    class Meta:
        db_table = "rh_accident_travail"

        verbose_name = "Accident de travail"

        verbose_name_plural = "Accidents de travail"

        ordering = (
            "-date_accident",
        )

        indexes = (
            models.Index(
                fields=("date_accident",),
            ),
        )

    def __str__(self):
        return (
            f"{self.agent} - "
            f"{self.date_accident:%d/%m/%Y}"
        )