"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : models/reprise_service.py

Description :
    Modèle de la reprise de service.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.db import models

from apps.rh.models import (
    BaseEvenementModel,
)


class RepriseService(
    BaseEvenementModel,
):
    """
    Informations spécifiques à une reprise de service.
    """

    date_reprise = models.DateField(
        verbose_name="Date de reprise",
        help_text=(
            "Date effective de reprise des fonctions."
        ),
    )

    observation = models.TextField(
        blank=True,
        default="",
        verbose_name="Observation",
    )

    class Meta:
        db_table = "rh_reprise_service"

        verbose_name = "Reprise de service"

        verbose_name_plural = "Reprises de service"

        ordering = (
            "-date_reprise",
        )

        indexes = (
            models.Index(
                fields=("date_reprise",),
            ),
        )

    def __str__(self):
        return (
            f"{self.agent} - "
            f"{self.date_reprise:%d/%m/%Y}"
        )