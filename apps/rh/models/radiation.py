# apps/rh/models/radiation.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : apps/rh/models/radiation.py

Description :
    Informations spécifiques à une radiation.

Auteur : SGCP
Version : 2.0
==========================================================
"""

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere


class Radiation(BaseStructureModel):
    """
    Radiation.

    Correspond à la radiation définitive
    d'un agent des effectifs de
    l'administration.

    Cet événement met fin définitivement
    à la carrière administrative de l'agent.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="radiation",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé.",
    )

    motif = models.TextField(
        blank=True,
        default="",
        verbose_name="Motif",
        help_text="Motif de la radiation.",
    )

    class Meta:
        db_table = "rh_radiation"

        verbose_name = "Radiation"
        verbose_name_plural = "Radiations"

        ordering = (
            "-id",
        )

        indexes = (

            models.Index(
                fields=("evenement",),
            ),

        )

    def __str__(self):
        return (
            f"{self.evenement.agent}"
        )