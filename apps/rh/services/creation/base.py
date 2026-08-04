"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/base.py

Description :
    Classe abstraite de base de tous les Creators
    du moteur de création.

Auteur : SGCP
Version : 2.2
==========================================================
"""

from abc import ABC, abstractmethod

from apps.rh.models.evenement import (
    EvenementCarriere,
)

from apps.rh.services.creation.context import (
    CreationContext,
)

from apps.rh.services.creation.exceptions import (
    DonneesEvenementInvalidesError,
)


class BaseEvenementCreator(ABC):
    """
    Classe abstraite de base de tous les Creators.

    Tous les Creators suivent le même cycle :

        create()
            ↓
        load_data()
            ↓
        validate()
            ↓
        before_create()
            ↓
        create_evenement()
            ↓
        process()
            ↓
        after_create()
            ↓
        audit()
    """

    def __init__(
        self,
        context: CreationContext,
    ):
        """
        Initialise le Creator.
        """

        self.context = context

    # =====================================================
    # Propriétés
    # =====================================================

    @property
    def validated_data(self):
        """
        Données validées.
        """
        return self.context.validated_data

    @property
    def payload(self):
        """
        Payload HTTP complet.
        """
        return self.context.payload

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
    def evenement(self):
        """
        Événement créé.
        """
        return self.context.evenement

    @property
    def agent(self):
        """
        Agent concerné.
        """
        return self.validated_data.get(
            "agent"
        )

    @property
    def type_evenement(self):
        """
        Type d'événement.
        """
        return self.validated_data.get(
            "type_evenement"
        )

    @property
    def code_evenement(self):
        """
        Code métier.
        """
        return self.type_evenement.code

    @property
    def date_effet(self):
        """
        Date d'effet.
        """
        return self.validated_data.get(
            "date_effet"
        )

    # =====================================================
    # Cycle de création
    # =====================================================

    def create(self):
        """
        Exécute le cycle complet
        de création.
        """

        try:

            self.load_data()

            self.validate()

            self.before_create()

            self.create_evenement()

            self.process()

            self.after_create()

            return self.evenement

        finally:

            self.audit()

    # =====================================================
    # Chargement des données spécialisées
    # =====================================================

    def load_data(self):
        """
        Charge les données spécialisées.

        Les Creators spécialisés peuvent
        redéfinir cette méthode pour charger
        les informations propres à leur
        événement.
        """
        pass

    # =====================================================
    # Validation commune
    # =====================================================

    def validate(self):
        """
        Validations communes.
        """

        if self.agent is None:
            raise DonneesEvenementInvalidesError(
                "L'agent est obligatoire."
            )

        if self.type_evenement is None:
            raise DonneesEvenementInvalidesError(
                "Le type d'événement est obligatoire."
            )

        if self.date_effet is None:
            raise DonneesEvenementInvalidesError(
                "La date d'effet est obligatoire."
            )

    # =====================================================
    # Création de l'événement
    # =====================================================

    def _build_evenement_data(self):
        """
        Prépare les données de création
        de l'événement.

        Retourne une copie des données
        validées afin de préserver
        l'intégrité du contexte.
        """

        return dict(
            self.validated_data
        )

    def create_evenement(self):
        """
        Crée l'événement de carrière.

        Cette méthode ne doit pas être
        redéfinie par les Creators.
        Tous les événements de carrière
        sont créés de manière uniforme.
        """

        self.context.evenement = (
            EvenementCarriere.objects.create(
                **self._build_evenement_data()
            )
        )

        return self.context.evenement

    # =====================================================
    # Hooks
    # =====================================================

    def before_create(self):
        """
        Hook exécuté avant la création.
        """
        pass

    @abstractmethod
    def process(self):
        """
        Crée les données spécialisées
        de l'événement.
        """
        raise NotImplementedError

    def after_create(self):
        """
        Hook exécuté après la création.
        """
        pass

    def audit(self):
        """
        Hook de journalisation.

        Sera utilisé ultérieurement pour :

            - journal d'audit ;
            - notifications ;
            - signature électronique ;
            - historique.
        """
        pass