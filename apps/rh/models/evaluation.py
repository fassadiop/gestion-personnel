# apps/rh/models/evaluation.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/rh/models/evaluation.py

Description :
    Gestion des évaluations professionnelles annuelles
    des agents.

Une évaluation constitue une appréciation de la
performance professionnelle d'un agent.

Elle enrichit le dossier administratif de l'agent mais
ne constitue jamais un événement de carrière.

Elle peut servir d'aide à la décision pour :

    - Reclassement
    - Avancement
    - Formation
    - Mobilité
    - Promotion

Auteur : SGCP
Version : 1.0
==========================================================
"""

from decimal import Decimal

from django.conf import settings
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models

from apps.rh.core.base import BaseModel
from apps.rh.models.affectation import Affectation
from apps.rh.models.agent import Agent
from apps.rh.models.organisation import Structure


# ==========================================================
# Constantes métier
# ==========================================================

COEF_QUALITES_PROFESSIONNELLES = Decimal("2")
COEF_COMPORTEMENT_TRAVAIL = Decimal("2")
COEF_RENDEMENT = Decimal("3")
COEF_CAPACITE_INITIATIVE = Decimal("3")

NOTE_MIN = Decimal("0")
NOTE_MAX = Decimal("20")

NOTE_VALIDATORS = (
    MinValueValidator(NOTE_MIN),
    MaxValueValidator(NOTE_MAX),
)


# ==========================================================
# Evaluation
# ==========================================================

class Evaluation(BaseModel):
    """
    Évaluation annuelle d'un agent.

    Une évaluation représente une appréciation
    professionnelle réalisée par la hiérarchie.

    Elle enrichit le dossier administratif mais ne
    modifie jamais directement la carrière de l'agent.
    """

    class Statut(models.TextChoices):
        BROUILLON = "BROUILLON", "Brouillon"
        SOUMISE = "SOUMISE", "Soumise"
        VALIDEE = "VALIDEE", "Validée"
        TRANSMISE = (
            "TRANSMISE",
            "Transmise à la Fonction Publique",
        )
        ARCHIVEE = "ARCHIVEE", "Archivée"

    # ======================================================
    # Informations générales
    # ======================================================

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="evaluations",
        verbose_name="Structure",
    )

    agent = models.ForeignKey(
        Agent,
        on_delete=models.PROTECT,
        related_name="evaluations",
        verbose_name="Agent",
    )

    affectation = models.ForeignKey(
        Affectation,
        on_delete=models.PROTECT,
        related_name="evaluations",
        verbose_name="Affectation",
    )

    evaluateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="evaluations_realisees",
        verbose_name="Évaluateur",
    )

    valide_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="evaluations_validees",
        null=True,
        blank=True,
        verbose_name="Validé par",
    )

    annee_evaluation = models.PositiveSmallIntegerField(
        verbose_name="Année d'évaluation",
    )

    date_evaluation = models.DateTimeField(
        verbose_name="Date de l'évaluation",
    )

    date_validation = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Date de validation",
    )

    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.BROUILLON,
        verbose_name="Statut",
    )

    # ======================================================
    # Notes
    # ======================================================

    note_qualites_professionnelles = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=NOTE_VALIDATORS,
        verbose_name="Qualités professionnelles",
    )

    note_comportement_travail = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=NOTE_VALIDATORS,
        verbose_name="Comportement au travail",
    )

    note_rendement = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=NOTE_VALIDATORS,
        verbose_name="Rendement",
    )

    note_capacite_initiative = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=NOTE_VALIDATORS,
        verbose_name="Capacité d'initiative",
    )

    # ======================================================
    # Observations
    # ======================================================

    points_forts = models.TextField(
        blank=True,
        verbose_name="Points forts",
    )

    points_amelioration = models.TextField(
        blank=True,
        verbose_name="Points à améliorer",
    )

    formation_souhaitee_agent = models.TextField(
        blank=True,
        verbose_name="Formation souhaitée par l'agent",
    )

    formation_recommandee_superieur = models.TextField(
        blank=True,
        verbose_name="Formation recommandée",
    )

    perspectives_carriere = models.TextField(
        blank=True,
        verbose_name="Perspectives de carrière",
    )

        # ======================================================
    # Meta
    # ======================================================

    class Meta:
        verbose_name = "Évaluation"
        verbose_name_plural = "Évaluations"

        ordering = (
            "-annee_evaluation",
            "agent",
        )

        indexes = [
            models.Index(
                fields=["structure"],
                name="idx_eval_structure",
            ),
            models.Index(
                fields=["agent"],
                name="idx_eval_agent",
            ),
            models.Index(
                fields=["evaluateur"],
                name="idx_eval_evaluateur",
            ),
            models.Index(
                fields=["annee_evaluation"],
                name="idx_eval_annee",
            ),
            models.Index(
                fields=["statut"],
                name="idx_eval_statut",
            ),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "agent",
                    "annee_evaluation",
                ],
                name="uq_eval_agent_annee",
            ),
        ]

    # ======================================================
    # Propriétés calculées
    # ======================================================

    @property
    def total_points(self):
        """
        Retourne le total pondéré obtenu par l'agent.

        Le calcul est effectué selon les coefficients
        officiels de la fiche d'évaluation.

        Qualités professionnelles : coefficient 2
        Comportement au travail   : coefficient 2
        Rendement                 : coefficient 3
        Initiative                : coefficient 3
        """

        return (
            (
                self.note_qualites_professionnelles
                * COEF_QUALITES_PROFESSIONNELLES
            )
            + (
                self.note_comportement_travail
                * COEF_COMPORTEMENT_TRAVAIL
            )
            + (
                self.note_rendement
                * COEF_RENDEMENT
            )
            + (
                self.note_capacite_initiative
                * COEF_CAPACITE_INITIATIVE
            )
        )

    @property
    def moyenne(self):
        """
        Retourne la moyenne générale sur 20.

        Les coefficients totalisent 10.

        Exemple :

            Total = 184,50

            Moyenne = 18,45
        """

        return (
            self.total_points / Decimal("10")
        ).quantize(
            Decimal("0.01")
        )

    # ======================================================
    # Représentation
    # ======================================================

    def __str__(self):
        return (
            f"Évaluation "
            f"{self.annee_evaluation} - "
            f"{self.agent}"
        )