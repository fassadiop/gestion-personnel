from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import Poste


class Interim(BaseStructureModel):
    """
    Intérim.

    Correspond à l'occupation temporaire
    d'un poste par un agent.

    Cet événement crée une occupation
    temporaire de poste.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="interim",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé.",
    )

    poste = models.ForeignKey(
        Poste,
        on_delete=models.PROTECT,
        related_name="interims",
        verbose_name="Poste",
        help_text="Poste assuré par intérim.",
    )

    class Meta:
        db_table = "rh_interim"

        verbose_name = "Intérim"
        verbose_name_plural = "Intérims"

        ordering = (
            "-id",
        )

        indexes = (
            models.Index(fields=("evenement",)),
            models.Index(fields=("poste",)),
        )

    def __str__(self):
        return (
            f"{self.evenement.agent} - "
            f"{self.poste}"
        )