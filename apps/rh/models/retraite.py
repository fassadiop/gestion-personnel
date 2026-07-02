# apps/rh/models/retraite.py

from django.db import models

from apps.rh.models.base_evenement import BaseEvenementModel

from apps.rh.models.referentiels import PositionAdministrative


class Retraite(BaseEvenementModel):
    """
    Informations spécifiques à une retraite.

    La retraite met définitivement fin à la
    carrière administrative de l'agent.

    Elle entraîne une nouvelle situation
    administrative sans création d'une
    nouvelle affectation ni d'une nouvelle
    occupation de poste.
    """

    position_administrative = models.ForeignKey(
        PositionAdministrative,
        on_delete=models.PROTECT,
        related_name="retraites",
        verbose_name="Position administrative",
        help_text="Position administrative correspondant à la retraite.",
    )

    date_depart = models.DateField(
        verbose_name="Date de départ à la retraite",
        help_text="Date effective de départ à la retraite.",
    )

    class Meta:
        db_table = "rh_retraite"

        verbose_name = "Retraite"
        verbose_name_plural = "Retraites"

        ordering = [
            "-date_depart",
            "-id",
        ]

        indexes = [

            models.Index(fields=["position_administrative"]),

            models.Index(fields=["date_depart"]),

        ]

    def __str__(self):

        return (
            f"Retraite de {self.evenement.agent}"
        )