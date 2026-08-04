# apps/rh/models/nomination.py

# apps/rh/models/nomination.py

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Structure,
    UniteOrganisationnelle,
    Poste,
)


class Nomination(BaseStructureModel):
    """
    Informations spécifiques à une nomination.

    Une nomination entraîne l'occupation
    d'un nouveau poste.

    Elle peut également modifier la structure
    ou l'unité organisationnelle.

    Les anciennes informations sont déjà
    historisées dans Affectation et
    OccupationPoste.

    Ce modèle ne contient donc que les
    nouvelles informations.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="nomination",
        verbose_name="Événement de carrière",
        help_text="Événement de nomination.",
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="nominations",
        verbose_name="Nouvelle structure",
    )

    unite = models.ForeignKey(
        UniteOrganisationnelle,
        on_delete=models.PROTECT,
        related_name="nominations",
        verbose_name="Nouvelle unité organisationnelle",
        null=True,
        blank=True,
    )

    poste = models.ForeignKey(
        Poste,
        on_delete=models.PROTECT,
        related_name="nominations",
        verbose_name="Nouveau poste",
    )

    class Meta:
        db_table = "rh_nomination"

        verbose_name = "Nomination"
        verbose_name_plural = "Nominations"

        ordering = [
            "-id",
        ]

        indexes = [

            models.Index(fields=["structure"]),

            models.Index(fields=["poste"]),

        ]

    def __str__(self):
        return (
            f"Nomination de {self.evenement.agent}"
        )