"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : models/mouvement_compteur_conge.py

Description :
    Historique des mouvements d'un compteur
    de congé.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.db import models

from apps.rh.core.base import BaseModel

from apps.rh.models.compteur_conge import (
    CompteurConge,
)

from apps.rh.models.referentiels import (
    TypeMouvementConge,
)


class MouvementCompteurConge(
    BaseModel,
):
    """
    Représente un mouvement effectué
    sur un compteur de congé.

    Chaque mouvement est historisé
    et ne doit jamais être modifié
    après validation.

    Les mouvements permettent de
    reconstituer intégralement
    l'historique d'un compteur.
    """

    compteur = models.ForeignKey(
        CompteurConge,
        on_delete=models.CASCADE,
        related_name="mouvements",
        verbose_name="Compteur de congé",
        help_text="Compteur concerné.",
    )

    type_mouvement = models.ForeignKey(
        TypeMouvementConge,
        on_delete=models.PROTECT,
        related_name="mouvements",
        verbose_name="Type de mouvement",
        help_text="Nature du mouvement.",
    )

    nombre_jours = models.PositiveSmallIntegerField(
        verbose_name="Nombre de jours",
        help_text="Nombre de jours concernés par le mouvement.",
    )

    date_mouvement = models.DateField(
        verbose_name="Date du mouvement",
        help_text="Date d'effet du mouvement.",
    )

    observation = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observation",
        help_text="Observation éventuelle.",
    )

    class Meta:
        db_table = "rh_mouvement_compteur_conge"

        verbose_name = (
            "Mouvement de compteur de congé"
        )

        verbose_name_plural = (
            "Mouvements de compteur de congé"
        )

        ordering = (
            "-date_mouvement",
            "-id",
        )

        constraints = (
            models.CheckConstraint(
                condition=models.Q(
                    nombre_jours__gt=0
                ),
                name=(
                    "ck_mouvement_compteur_conge_nombre_jours"
                ),
            ),
        )

        indexes = (
            models.Index(fields=("compteur",)),
            models.Index(fields=("type_mouvement",)),
            models.Index(fields=("date_mouvement",)),
        )

    def __str__(self):
        return (
            f"{self.compteur.agent} - "
            f"{self.type_mouvement.libelle} "
            f"({self.nombre_jours} jours)"
        )

    # ==========================================================
    # PROPRIÉTÉS MÉTIER
    # ==========================================================

    @property
    def agent(self):
        """
        Agent concerné.
        """
        return self.compteur.agent

    @property
    def decision_conge(self):
        """
        Décision de congé concernée.
        """
        return self.compteur.decision_conge

    @property
    def sens(self):
        """
        Sens du mouvement.

        +1 = Crédit
        -1 = Débit
        """
        return self.type_mouvement.sens

    @property
    def impact(self):
        """
        Impact signé du mouvement
        sur le compteur.
        """
        return (
            self.nombre_jours
            * self.sens
        )