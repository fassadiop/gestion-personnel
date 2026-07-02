# apps/rh/models/mission.py

from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db import models
from apps.rh.models.base_evenement import BaseEvenementModel
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.referentiels import (
    Pays,
    SourceFinancement,
    TypeMission,
)


class Mission(BaseEvenementModel):
    """
    Mission effectuée par un agent.

    Une mission constitue la spécialisation d'un
    événement de carrière.

    Les informations communes (agent, structure,
    dates, acte administratif, position administrative...)
    sont portées par EvenementCarriere.

    Cette entité ne contient que les informations
    spécifiques à la mission.
    """

    type_mission = models.ForeignKey(
        TypeMission,
        on_delete=models.PROTECT,
        related_name="missions",
        verbose_name="Type de mission",
        help_text="Nature de la mission.",
    )

    pays = models.ForeignKey(
        Pays,
        on_delete=models.PROTECT,
        related_name="missions",
        verbose_name="Pays",
        help_text="Pays de déroulement de la mission.",
    )

    ville = models.CharField(
        max_length=150,
        verbose_name="Ville",
        help_text="Ville de déroulement de la mission.",
    )

    organisme_accueil = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Organisme d'accueil",
        help_text="Organisme ou institution d'accueil.",
    )

    source_financement = models.ForeignKey(
        SourceFinancement,
        on_delete=models.PROTECT,
        related_name="missions",
        null=True,
        blank=True,
        verbose_name="Source de financement",
        help_text="Source de financement de la mission.",
    )

    cout = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=Decimal("0.00"),
        verbose_name="Coût",
        help_text="Coût global estimé ou réel de la mission.",
    )

    rapport_remis = models.BooleanField(
        default=False,
        verbose_name="Rapport remis",
        help_text="Indique si le rapport de mission a été remis.",
    )

    class Meta:
        db_table = "rh_mission"

        verbose_name = "Mission"
        verbose_name_plural = "Missions"

        ordering = [
            "-evenement__date_effet",
            "pays__libelle",
            "ville",
        ]

        constraints = [

            models.CheckConstraint(
                condition=models.Q(cout__gte=0),
                name="ck_mission_cout_positif",
            ),

        ]

        indexes = [

            models.Index(fields=["type_mission"]),

            models.Index(fields=["pays"]),

            models.Index(fields=["ville"]),

            models.Index(fields=["source_financement"]),

            models.Index(fields=["rapport_remis"]),

        ]

    def __str__(self):
        return (
            f"{self.evenement.objet} "
            f"({self.pays.libelle} - {self.ville})"
        )
    
    def clean(self):
        """
        Validations métier.
        """
        super().clean()

        # Le coût ne peut pas être négatif.
        if self.cout is not None and self.cout < 0:
            raise ValidationError(
                {
                    "cout": (
                        "Le coût de la mission ne peut pas être négatif."
                    )
                }
            )

    @property
    def duree(self):
        """
        Durée de la mission en jours.

        Retourne None si la mission est toujours en cours.
        """
        if self.evenement.date_fin is None:
            return None

        return (
            self.evenement.date_fin
            - self.evenement.date_effet
        ).days

    @property
    def est_en_cours(self):
        """
        Indique si la mission est toujours en cours.
        """
        return self.evenement.date_fin is None

    @property
    def est_terminee(self):
        """
        Indique si la mission est terminée.
        """
        return not self.est_en_cours