"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/base.py

Description :
    Classe abstraite de base de tous les handlers
    du moteur de carrière.

Auteur : SGCP
Version : 2.2
==========================================================
"""

from abc import ABC, abstractmethod
from apps.rh.models import StatutEvenement
from apps.rh.services.evenements.context import (
    ExecutionContext,
)

from apps.rh.services.evenements.exceptions import (
    EvenementInvalideError,
    StatutEvenementInvalideError,
)


class BaseEvenementHandler(ABC):
    """
    Classe abstraite de base de tous les handlers
    du moteur de carrière.

    Tous les handlers suivent le même cycle :

        execute()
            ↓
        load_context()
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

    Les handlers spécialisés implémentent
    uniquement la méthode process().
    """

    def __init__(
        self,
        context: ExecutionContext,
    ):
        """
        Initialise le handler.
        """

        self.context = context

        self._situation = None
        self._affectation = None
        self._occupation = None

    # =====================================================
    # Propriétés
    # =====================================================

    @property
    def evenement(self):
        """
        Événement courant.
        """
        return self.context.evenement

    @property
    def utilisateur(self):
        """
        Utilisateur courant.
        """
        return self.context.utilisateur

    @property
    def request(self):
        """
        Requête HTTP.
        """
        return self.context.request

    @property
    def agent(self):
        """
        Agent concerné.
        """
        return self.evenement.agent

    @property
    def type_evenement(self):
        """
        Type d'événement.
        """
        return self.evenement.type_evenement

    @property
    def code_evenement(self):
        """
        Code métier.
        """
        return self.type_evenement.code

    @property
    def statut(self):
        """
        Code du statut.
        """
        return self.evenement.statut.code

    @property
    def date_effet(self):
        """
        Date d'effet.
        """
        return self.evenement.date_effet

    @property
    def reference_acte(self):
        """
        Référence administrative.
        """
        return self.evenement.reference_acte

    @property
    def situation(self):
        """
        Situation administrative courante.
        """
        return self._situation

    @property
    def affectation(self):
        """
        Affectation courante.
        """
        return self._affectation

    @property
    def occupation(self):
        """
        Occupation principale de poste.
        """
        return self._occupation

    # =====================================================
    # Chargement du contexte
    # =====================================================

    def load_context(self):
        """
        Charge le contexte courant
        de l'agent.
        """

        print("===== LOAD CONTEXT =====")
        print("Agent :", self.agent.id)

        self._situation = (
            self.agent.situation_administrative_courante
        )

        print("Situation chargée :", self._situation)

        self._affectation = (
            self.agent.affectation_courante
        )

        self._occupation = (
            self.agent.occupations_poste.filter(
                date_fin__isnull=True,
                est_interim=False,
            ).first()
        )

    def get_evenement_data(
        self,
        relation_name: str,
        model_class,
    ):
        """
        Retourne les données spécialisées
        d'un événement.

        Recherche d'abord une relation métier
        explicite (ex. : evenement.conge),
        puis, à défaut, la relation générée
        automatiquement par BaseEvenementModel
        (ex. : evenement.rh_conge).
        """

        # ==========================================
        # 1. Relation métier explicite
        # ==========================================

        if hasattr(
            self.evenement,
            relation_name,
        ):
            return getattr(
                self.evenement,
                relation_name,
            )

        # ==========================================
        # 2. Relation générée automatiquement
        # ==========================================

        generated_relation = (
            f"{model_class._meta.app_label}_"
            f"{model_class._meta.model_name}"
        )

        if hasattr(
            self.evenement,
            generated_relation,
        ):
            return getattr(
                self.evenement,
                generated_relation,
            )

        # ==========================================
        # 3. Aucune relation trouvée
        # ==========================================

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
        Exécute le cycle complet
        du handler.
        """

        try:

            self.load_context()

            self.validate()

            self.before_execute()

            result = self.process()

            self._marquer_evenement_valide()

            self.after_execute()

            return result

        finally:

            self.audit()

    # =====================================================
    # Validation commune
    # =====================================================

    def validate(self):
        """
        Validations communes.
        """

        if self.evenement is None:
            raise EvenementInvalideError(
                "Aucun événement fourni."
            )

        if self.agent is None:
            raise EvenementInvalideError(
                "Aucun agent associé à l'événement."
            )

        if self.type_evenement is None:
            raise EvenementInvalideError(
                "Le type d'événement est obligatoire."
            )

        if self.date_effet is None:
            raise EvenementInvalideError(
                "La date d'effet est obligatoire."
            )

        if not self.evenement.actif:
            raise EvenementInvalideError(
                "L'événement est inactif."
            )

        if self.statut != "EN_ATTENTE":
            raise StatutEvenementInvalideError(
                "Seuls les événements en attente "
                "peuvent être exécutés."
            )
        
    def _marquer_evenement_valide(self):
        """
        Marque l'événement comme validé.
        """

        statut_valide = StatutEvenement.objects.get(
            code="VALIDE"
        )

        self.evenement.statut = statut_valide

        self.evenement.save(
            update_fields=["statut"]
        )

    # =====================================================
    # Hooks
    # =====================================================

    def before_execute(self):
        """
        Hook exécuté avant
        le traitement métier.
        """
        pass

    @abstractmethod
    def process(self):
        """
        Traitement métier.

        À implémenter dans tous
        les handlers.
        """
        raise NotImplementedError

    def after_execute(self):
        """
        Hook exécuté après
        le traitement métier.
        """
        pass

    def audit(self):
        """
        Hook de journalisation.

        Sera utilisé ultérieurement pour :

            - Journal d'audit
            - Notifications
            - Signature électronique
            - Historique
        """
        pass