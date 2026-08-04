# apps/rh/models/decision_conge.py

from django.db import models

from apps.rh.core.base import BaseModel
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.referentiels import TypeConge


class DecisionConge(BaseModel):
    """
    Décision administrative accordant un congé.

    Cette entité matérialise l'acte administratif qui ouvre
    un droit à congé pour un agent.

    Une décision peut donner lieu à une ou plusieurs
    périodes de jouissance (fractionnement).

    Les informations communes (agent, acte administratif,
    autorité signataire, dates, etc.) sont portées par
    EvenementCarriere.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.CASCADE,
        related_name="decision_conge",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé à cette décision.",
    )

    type_conge = models.ForeignKey(
        TypeConge,
        on_delete=models.PROTECT,
        related_name="decisions_conge",
        verbose_name="Type de congé",
        help_text="Type de congé accordé.",
    )

    nombre_jours_accordes = models.PositiveSmallIntegerField(
        verbose_name="Nombre de jours accordés",
        help_text="Nombre total de jours accordés par la décision.",
    )

    class Meta:
        db_table = "rh_decision_conge"

        verbose_name = "Décision de congé"
        verbose_name_plural = "Décisions de congé"

        ordering = (
            "-evenement__date_effet",
            "type_conge__libelle",
        )

        constraints = (
            models.CheckConstraint(
                condition=models.Q(
                    nombre_jours_accordes__gt=0
                ),
                name="ck_decision_conge_nombre_jours_positif",
            ),
        )

        indexes = (
            models.Index(fields=("type_conge",)),
        )

    def __str__(self):
        return (
            f"{self.type_conge.libelle} - "
            f"{self.agent}"
        )

    # ==========================================================
    # PROPRIÉTÉS MÉTIER
    # ==========================================================

    @property
    def agent(self):
        """
        Agent bénéficiaire de la décision de congé.
        """
        return self.evenement.agent

    @property
    def structure(self):
        """
        Structure d'affectation de l'agent au moment
        de la décision.
        """
        return self.evenement.structure

    @property
    def date_decision(self):
        """
        Date de signature de la décision.
        """
        return self.evenement.date_acte

    @property
    def date_effet(self):
        """
        Date d'effet de la décision.
        """
        return self.evenement.date_effet

    @property
    def tranches(self):
        """
        Retourne les périodes de jouissance
        classées chronologiquement.
        """
        return (
            self.conges
            .filter(actif=True)
            .order_by("date_cessation_service")
        )

    @property
    def nombre_jours_consommes(self):
        """
        Nombre total de jours déjà consommés
        au titre de cette décision.
        """
        return sum(
            conge.nombre_jours
            for conge in self.tranches
        )

    @property
    def reliquat(self):
        """
        Nombre de jours restant à consommer.
        """
        return max(
            0,
            self.nombre_jours_accordes
            - self.nombre_jours_consommes,
        )

    @property
    def est_soldee(self):
        """
        Indique si tous les jours accordés
        ont été consommés.
        """
        return self.reliquat == 0