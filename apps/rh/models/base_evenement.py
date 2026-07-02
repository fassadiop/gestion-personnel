# apps/rh/models/base_evenement.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : apps/rh/models/base_evenement.py

Description :
    Classe abstraite de base des spécialisations
    d'un événement de carrière.

    Toutes les entités métier représentant une
    spécialisation d'EvenementCarriere héritent
    de cette classe.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.db import models

from apps.rh.core.base import BaseModel
from apps.rh.models.evenement import EvenementCarriere


class BaseEvenementModel(BaseModel):
    """
    Classe abstraite des spécialisations
    d'un événement de carrière.

    Les informations communes (agent,
    structure, dates, position administrative,
    acte administratif...) sont portées par
    EvenementCarriere.

    Cette classe fournit un accès unifié à ces
    informations afin d'éviter leur duplication
    dans tous les modules spécialisés.
    """

    evenement = models.OneToOneField(
        EvenementCarriere,
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s",
        verbose_name="Événement de carrière",
        help_text="Événement de carrière associé.",
    )

    class Meta:
        abstract = True

    # ======================================================
    # Propriétés communes
    # ======================================================

    @property
    def agent(self):
        """
        Agent concerné.
        """
        return self.evenement.agent

    @property
    def structure(self):
        """
        Structure de rattachement.
        """
        return self.evenement.structure

    @property
    def position_administrative(self):
        """
        Position administrative résultante.
        """
        return self.evenement.position_administrative

    @property
    def date_effet(self):
        """
        Date d'effet de l'événement.
        """
        return self.evenement.date_effet

    @property
    def date_fin(self):
        """
        Date de fin de l'événement.
        """
        return self.evenement.date_fin

    @property
    def numero_acte(self):
        """
        Numéro officiel de l'acte administratif.
        """
        return self.evenement.numero_acte

    @property
    def date_acte(self):
        """
        Date de signature de l'acte.
        """
        return self.evenement.date_acte

    @property
    def reference_acte(self):
        """
        Référence complète de l'acte.
        """
        return self.evenement.reference_acte

    @property
    def autorite_signataire(self):
        """
        Autorité signataire.
        """
        return self.evenement.autorite_signataire

    @property
    def documents(self):
        """
        Documents administratifs associés.
        """
        return self.evenement.documents.all()

    def __str__(self):
        return str(self.evenement)