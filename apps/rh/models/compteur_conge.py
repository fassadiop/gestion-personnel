# apps/rh/models/compteur_conge.py

from django.db import models

from apps.rh.core.base import BaseModel
from apps.rh.models.decision_conge import (
    DecisionConge,
)


class CompteurConge(BaseModel):
    """
    Compteur de consommation d'une décision de congé.

    Chaque décision de congé ouvre un compteur unique.

    Le compteur centralise l'état de consommation
    de la décision et sert de point d'entrée
    aux mouvements de consommation.
    """

    decision_conge = models.OneToOneField(
        DecisionConge,
        on_delete=models.CASCADE,
        related_name="compteur",
        verbose_name="Décision de congé",
        help_text=(
            "Décision de congé ouvrant le droit."
        ),
    )

    class Meta:
        db_table = "rh_compteur_conge"

        verbose_name = "Compteur de congé"

        verbose_name_plural = (
            "Compteurs de congé"
        )

    def __str__(self):
        return (
            f"{self.agent} - "
            f"{self.decision_conge.type_conge.libelle}"
        )

    # ==========================================================
    # PROPRIÉTÉS MÉTIER
    # ==========================================================

    @property
    def agent(self):
        """
        Agent concerné.
        """
        return (
            self.decision_conge.agent
        )

    @property
    def type_conge(self):
        """
        Type de congé.
        """
        return (
            self.decision_conge.type_conge
        )

    @property
    def jours_accordes(self):
        """
        Nombre de jours accordés.
        """
        return (
            self.decision_conge
            .nombre_jours_accordes
        )

    @property
    def jours_credites(self):
        """
        Nombre total de jours crédités
        sur le compteur.
        """
        return sum(
            mouvement.nombre_jours
            for mouvement in self.mouvements.filter(
                actif=True,
                type_mouvement__sens=1,
            )
        )

    @property
    def jours_debites(self):
        """
        Nombre total de jours débités
        du compteur.
        """
        return sum(
            mouvement.nombre_jours
            for mouvement in self.mouvements.filter(
                actif=True,
                type_mouvement__sens=-1,
            )
        )

    @property
    def jours_consommes(self):
        """
        Nombre total de jours consommés.

        Correspond aux mouvements
        de débit du compteur.
        """
        return self.jours_debites

    @property
    def reliquat(self):
        """
        Nombre de jours restant.
        """
        return max(
            0,
            self.jours_credites
            - self.jours_debites,
        )

    @property
    def est_solde(self):
        """
        Indique si le compteur
        est entièrement consommé.
        """
        return (
            self.reliquat == 0
        )