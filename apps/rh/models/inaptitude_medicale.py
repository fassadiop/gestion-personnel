# apps/rh/models/inaptitude_medicale.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : apps/rh/models/inaptitude_medicale.py

Description :
    Modèle de l'inaptitude médicale.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.db import models

from apps.rh.models import (
    BaseEvenementModel,
)

from apps.rh.models.referentiels import (
    TypeInaptitudeMedicale,
)


class InaptitudeMedicale(
    BaseEvenementModel,
):
    """
    Informations spécifiques à une décision
    d'inaptitude médicale.
    """

    type_inaptitude = models.ForeignKey(
        TypeInaptitudeMedicale,
        on_delete=models.PROTECT,
        related_name="inaptitudes_medicales",
        verbose_name="Type d'inaptitude",
    )

    date_effet = models.DateField(
        verbose_name="Date d'effet",
        help_text=(
            "Date de prise d'effet de la décision "
            "d'inaptitude."
        ),
    )

    date_fin = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de fin",
        help_text=(
            "Date de fin de l'inaptitude lorsqu'elle "
            "est temporaire."
        ),
    )

    observation = models.TextField(
        blank=True,
        default="",
        verbose_name="Observation",
    )

    class Meta:
        db_table = "rh_inaptitude_medicale"

        verbose_name = (
            "Inaptitude médicale"
        )

        verbose_name_plural = (
            "Inaptitudes médicales"
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
                    "ck_inaptitude_medicale_dates"
                ),
            ),

        )

        indexes = (

            models.Index(
                fields=(
                    "type_inaptitude",
                )
            ),

            models.Index(
                fields=(
                    "date_effet",
                )
            ),

        )

    def __str__(self):
        return (
            f"{self.agent} - "
            f"{self.type_inaptitude}"
        )