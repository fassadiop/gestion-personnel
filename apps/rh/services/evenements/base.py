"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/base.py

Description :
    Classe abstraite de base de tous les handlers
    du moteur de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from abc import ABC, abstractmethod

from apps.rh.services.evenements.exceptions import (
    EvenementInvalideError,
    StatutEvenementInvalideError,
)


class BaseEvenementHandler(ABC):
    """
    Classe abstraite de base de tous les handlers
    du moteur de carrière.

    Chaque événement suit exactement le même cycle
    d'exécution :

        execute()
            ↓
        validate()
            ↓
        before_execute()
            ↓
        process()
            ↓
        after_execute()
            ↓
        audit()

    Les classes filles ne redéfinissent généralement
    que la méthode process().
    """

    def __init__(self, evenement):
        """
        Initialise le handler.

        Args:
            evenement:
                Instance de EvenementCarriere.
        """

        self.evenement = evenement

        # Contexte partagé entre les différentes
        # étapes du traitement.
        self.context = {}

    # =====================================================
    # Propriétés
    # =====================================================

    @property
    def agent(self):
        """Agent concerné."""
        return self.evenement.agent

    @property
    def type_evenement(self):
        """Type d'événement."""
        return self.evenement.type_evenement

    @property
    def code_evenement(self):
        """Code métier de l'événement."""
        return self.type_evenement.code

    @property
    def statut(self):
        """Code du statut."""
        return self.evenement.statut.code

    @property
    def date_effet(self):
        """Date d'effet."""
        return self.evenement.date_effet

    @property
    def reference(self):
        """Référence administrative."""
        return self.evenement.reference

    @property
    def utilisateur(self):
        """
        Utilisateur ayant validé
        l'événement.
        """

        return getattr(
            self.evenement,
            "valide_par",
            None,
        )
    
    def load_evenement_data(
        self,
        relation_name: str,
        model_class,
    ):
        """
        Charge les données spécialisées d'un événement.

        Args:
            relation_name:
                Nom de la relation OneToOne portée
                par EvenementCarriere.

            model_class:
                Classe du modèle attendu.

        Returns:
            Instance du modèle spécialisé.

        Raises:
            EvenementInvalideError
        """

        try:
            return getattr(
                self.evenement,
                relation_name,
            )

        except model_class.DoesNotExist:
            raise EvenementInvalideError(
                f"Les informations de "
                f"{relation_name.replace('_', ' ')} "
                "sont absentes."
            )

    # =====================================================
    # Cycle d'exécution
    # =====================================================

    def execute(self):
        """
        Exécute le cycle complet du handler.

        Cette méthode ne doit jamais être
        redéfinie.
        """

        self.validate()

        self.before_execute()

        result = self.process()

        self.after_execute()

        self.audit()

        return result

    # =====================================================
    # Validation commune
    # =====================================================

    def validate(self):
        """
        Validations communes.

        Les handlers spécialisés peuvent
        redéfinir cette méthode en appelant :

            super().validate()
        """

        if self.evenement is None:
            raise EvenementInvalideError(
                "Aucun événement fourni."
            )

        if self.agent is None:
            raise EvenementInvalideError(
                "Aucun agent associé à l'événement."
            )

        if not self.evenement.actif:
            raise EvenementInvalideError(
                "L'événement est inactif."
            )

        if self.statut != "VALIDE":
            raise StatutEvenementInvalideError(
                "Seuls les événements validés peuvent être exécutés."
            )

    # =====================================================
    # Hooks
    # =====================================================

    def before_execute(self):
        """
        Hook exécuté après validation.

        Sert principalement à préparer
        le contexte du traitement.

        Exemple :

            self.context["situation"] = ...
        """
        pass

    @abstractmethod
    def process(self):
        """
        Traitement métier.

        Cette méthode doit être implémentée
        par tous les handlers.

        Returns
        -------
        Any
            Résultat du traitement métier.
        """
        raise NotImplementedError

    def after_execute(self):
        """
        Hook exécuté après le traitement.

        Peut servir à effectuer
        des traitements complémentaires.
        """
        pass

    def audit(self):
        """
        Hook de journalisation.

        Cette méthode sera utilisée
        ultérieurement pour :

        - JournalAudit
        - Notifications
        - Signature électronique
        - Historique
        """
        pass