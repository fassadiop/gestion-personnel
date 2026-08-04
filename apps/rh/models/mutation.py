# apps/rh/models/mutation.py

# apps/rh/models/mutation.py

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Structure,
    UniteOrganisationnelle,
    Poste,
)


class Mutation(BaseStructureModel):
    """
    Informations spécifiques à une mutation.

    Une mutation entraîne un changement
    d'affectation et éventuellement
    un changement de poste.

    Les anciennes informations sont déjà
    historisées dans Affectation et
    OccupationPoste.

    Ce modèle ne contient donc que la
    nouvelle destination.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="mutation",
        verbose_name="Événement de carrière",
        help_text="Événement de mutation.",
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="mutations",
        verbose_name="Nouvelle structure",
    )

    unite = models.ForeignKey(
        UniteOrganisationnelle,
        on_delete=models.PROTECT,
        related_name="mutations",
        verbose_name="Nouvelle unité organisationnelle",
        null=True,
        blank=True,
    )

    poste = models.ForeignKey(
        Poste,
        on_delete=models.PROTECT,
        related_name="mutations",
        verbose_name="Nouveau poste",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "rh_mutation"

        verbose_name = "Mutation"
        verbose_name_plural = "Mutations"

        ordering = [
            "-id",
        ]

        indexes = [

            models.Index(fields=["structure"]),

            models.Index(fields=["poste"]),

        ]

    def __str__(self):
        return (
            f"Mutation de {self.evenement.agent}"
        )