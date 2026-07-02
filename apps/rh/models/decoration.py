# apps/rh/models/decoration.py

from django.db import models

from apps.rh.models.base_evenement import BaseEvenementModel
from apps.rh.models.referentiels import TypeDecoration


class Decoration(BaseEvenementModel):
    """
    Décoration ou distinction honorifique accordée à un agent.

    Cette entité représente une distinction officiellement
    accordée à un agent et devenue exécutoire.

    Les informations communes (agent, acte administratif,
    autorité signataire, dates, etc.) sont portées par
    EvenementCarriere.
    """

    type_decoration = models.ForeignKey(
        TypeDecoration,
        on_delete=models.PROTECT,
        related_name="decorations",
        verbose_name="Type de décoration",
        help_text="Nature de la distinction honorifique.",
    )

    date_faits = models.DateField(
        verbose_name="Date des faits",
        help_text=(
            "Date des faits ou de la période ayant motivé "
            "l'attribution de la décoration."
        ),
    )

    faits_remarquables = models.TextField(
        blank=True,
        default="",
        verbose_name="Faits remarquables",
        help_text=(
            "Description des faits ou mérites ayant conduit "
            "à l'attribution de la décoration."
        ),
    )

    date_remise = models.TextField(
        blank=True,
        default="",
        verbose_name="Date remise",
        help_text=(
            "Date remise de la décoration."
        ),
    )

    class Meta:
        db_table = "rh_decoration"

        verbose_name = "Décoration"
        verbose_name_plural = "Décorations"

        ordering = [
            "-evenement__date_effet",
            "type_decoration__libelle",
        ]

        indexes = [

            models.Index(fields=["type_decoration"]),

            models.Index(fields=["date_faits"]),

        ]

    def __str__(self):
        return (
            f"{self.type_decoration.libelle} "
            f"({self.agent})"
        )
