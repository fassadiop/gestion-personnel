# apps/rh/models/evenement.py

from django.db import models

from apps.rh.core.base import BaseLibelleModel, BaseStructureModel

from apps.rh.models.agent import Agent
from apps.rh.models.referentiels import (
    PositionAdministrative,
    StatutEvenement,
    TypeEvenement,
)


class EvenementCarriere(BaseStructureModel):
    """
    Événement de carrière.

    Représente toute décision administrative ayant un impact
    sur la carrière d'un agent.

    L'événement constitue le pivot du SGCP.

    Exemples :

    - Recrutement
    - Titularisation
    - Affectation
    - Mutation
    - Nomination
    - Promotion
    - Reclassement
    - Avancement
    - Congé
    - Absence
    - Mission
    - Formation
    - Sanction
    - Décoration
    - Retraite
    """

    agent = models.ForeignKey(
        Agent,
        on_delete=models.PROTECT,
        related_name="evenements",
        verbose_name="Agent",
        help_text="Agent concerné par l'événement.",
    )

    type_evenement = models.ForeignKey(
        TypeEvenement,
        on_delete=models.PROTECT,
        related_name="evenements",
        verbose_name="Type d'événement",
        help_text="Nature de l'événement de carrière.",
    )

    statut = models.ForeignKey(
        StatutEvenement,
        on_delete=models.PROTECT,
        related_name="evenements",
        verbose_name="Statut",
        help_text="Statut courant de l'événement.",
    )

    position_administrative = models.ForeignKey(
        PositionAdministrative,
        on_delete=models.PROTECT,
        related_name="evenements",
        verbose_name="Position administrative",
        help_text="Position administrative résultant de l'événement.",
    )

    date_effet = models.DateField(
        verbose_name="Date d'effet",
        help_text="Date officielle de prise d'effet.",
    )

    date_fin = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de fin",
        help_text="Date de fin d'effet lorsque applicable.",
    )

    numero_acte = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Numéro de l'acte",
        help_text="Numéro officiel de l'arrêté, décret, décision ou note.",
    )

    date_acte = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de l'acte",
        help_text="Date de signature de l'acte administratif.",
    )

    reference_acte = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Référence de l'acte",
        help_text="Référence complète de l'acte administratif.",
    )

    objet = models.CharField(
        max_length=255,
        verbose_name="Objet",
        help_text="Objet synthétique de l'événement.",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description",
        help_text="Description détaillée de l'événement.",
    )

    autorite_signataire = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Autorité signataire",
        help_text="Autorité ayant signé l'acte administratif.",
    )

    class Meta:
        db_table = "rh_evenement_carriere"

        verbose_name = "Événement de carrière"
        verbose_name_plural = "Événements de carrière"

        ordering = [
            "-date_effet",
            "-id",
        ]

        constraints = [

            models.CheckConstraint(
                condition=(
                    models.Q(date_fin__isnull=True)
                    |
                    models.Q(date_fin__gte=models.F("date_effet"))
                ),
                name="ck_evenement_dates",
            ),

        ]

        indexes = [

            models.Index(fields=["agent"]),

            models.Index(fields=["type_evenement"]),

            models.Index(fields=["statut"]),

            models.Index(fields=["position_administrative"]),

            models.Index(fields=["date_effet"]),

            models.Index(fields=["numero_acte"]),

        ]

    def __str__(self):

        return (
            f"{self.agent} - "
            f"{self.type_evenement.libelle} "
            f"({self.date_effet:%d/%m/%Y})"
        )
