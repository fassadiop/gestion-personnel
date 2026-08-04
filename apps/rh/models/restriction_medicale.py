"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : models/restriction_medicale.py

Description :
    Modèle de la restriction médicale.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.db import models

from apps.rh.models.base_evenement import (
    BaseEvenementModel,
)


class RestrictionMedicale(
    BaseEvenementModel,
):
    """
    Informations spécifiques à une décision
    de restriction médicale.
    """

    date_effet = models.DateField(
        verbose_name="Date d'effet",
        help_text=(
            "Date de prise d'effet de la restriction."
        ),
    )

    date_fin = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de fin",
        help_text=(
            "Date de fin de la restriction lorsqu'elle est temporaire."
        ),
    )

    restriction = models.TextField(
        verbose_name="Restriction",
        help_text=(
            "Description de la restriction administrative imposée à l'agent."
        ),
    )

    observation = models.TextField(
        blank=True,
        default="",
        verbose_name="Observation",
    )

    class Meta:
        db_table = "rh_restriction_medicale"

        verbose_name = (
            "Restriction médicale"
        )

        verbose_name_plural = (
            "Restrictions médicales"
        )

        ordering = (
            "-date_effet",
        )

        constraints = (

            models.CheckConstraint(
                condition=(
                    models.Q(date_fin__isnull=True)
                    |
                    models.Q(
                        date_fin__gte=models.F(
                            "date_effet"
                        )
                    )
                ),
                name=(
                    "ck_restriction_medicale_dates"
                ),
            ),

        )

        indexes = (

            models.Index(
                fields=("date_effet",)
            ),

        )

    def __str__(self):
        return (
            f"{self.agent} - "
            f"{self.date_effet:%d/%m/%Y}"
        )