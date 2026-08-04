# apps/rh/models/agent.py

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from apps.rh.core.base import BaseStructureModel
from apps.rh.models.organisation import Structure
from apps.rh.models.referentiels import (
    EtatCivil,
    Nationalite,
    StatutAgent,
    Sexe,
)


class Agent(BaseStructureModel):
    """
    Agent de la Fonction Publique.

    Cette entité contient uniquement les informations
    permanentes d'identification de l'agent.
    """

    statut = models.ForeignKey(
        StatutAgent,
        on_delete=models.PROTECT,
        related_name="agents",
        verbose_name="Statut",
        help_text="Statut juridique de l'agent.",
    )

    matricule = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="Matricule",
        help_text="Obligatoire pour les fonctionnaires.",
    )

    numero_solde = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="Numéro de solde",
        help_text="Obligatoire pour les contractuels.",
    )

    nom = models.CharField(
        max_length=100,
        verbose_name="Nom",
    )

    prenom = models.CharField(
        max_length=150,
        verbose_name="Prénom",
    )

    nom_jeune_fille = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Nom de jeune fille",
    )

    sexe = models.ForeignKey(
        Sexe,
        on_delete=models.PROTECT,
        related_name="agents",
        verbose_name="Sexe",
    )

    date_naissance = models.DateField(
        verbose_name="Date de naissance",
    )

    lieu_naissance = models.CharField(
        max_length=150,
        verbose_name="Lieu de naissance",
    )

    nationalite = models.ForeignKey(
        Nationalite,
        on_delete=models.PROTECT,
        related_name="agents",
        verbose_name="Nationalité",
    )

    etat_civil = models.ForeignKey(
        EtatCivil,
        on_delete=models.PROTECT,
        related_name="agents",
        verbose_name="État civil",
    )

    telephone = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="Téléphone",
    )

    email = models.EmailField(
        blank=True,
        verbose_name="Adresse e-mail",
    )

    adresse = models.TextField(
        blank=True,
        verbose_name="Adresse",
    )

    photo = models.ImageField(
        upload_to="agents/photos/",
        null=True,
        blank=True,
        verbose_name="Photo",
    )

    date_recrutement = models.DateField(
        verbose_name="Date de recrutement",
        help_text="Date d'entrée dans la Fonction Publique.",
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agent",
        verbose_name="Compte utilisateur",
        help_text="Compte utilisateur associé à l'agent.",
    )

    structure_racine = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="agents",
        verbose_name="Structure racine",
        help_text="Structure racine propriétaire du dossier de l'agent.",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "rh_agent"
        verbose_name = "Agent"
        verbose_name_plural = "Agents"
        ordering = ["nom", "prenom"]

        indexes = [
            models.Index(fields=["matricule"]),
            models.Index(fields=["numero_solde"]),
            models.Index(fields=["nom"]),
            models.Index(fields=["prenom"]),
            models.Index(fields=["structure_racine"]),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["matricule"],
                condition=models.Q(matricule__gt=""),
                name="uq_agent_matricule",
            ),
            models.UniqueConstraint(
                fields=["numero_solde"],
                condition=models.Q(numero_solde__gt=""),
                name="uq_agent_numero_solde",
            ),
        ]

    @property
    def situation_administrative_courante(self):
        """
        Retourne la situation administrative actuellement
        en vigueur de l'agent.
        """

        return (
            self.situations_administratives
            .filter(est_courante=True)
            .first()
        )

    @property
    def affectation_courante(self):
        """
        Retourne l'affectation actuellement en vigueur.
        """

        return (
            self.affectations
            .filter(est_courante=True)
            .first()
        )
    
    @property
    def compteur_conge_actif(self):
        """
        Retourne le plus ancien compteur
        de congé disponible.
        """

        from apps.rh.models.compteur_conge import (
            CompteurConge,
        )

        compteurs = (
            CompteurConge.objects
            .filter(
                decision_conge__evenement__agent=self,
                actif=True,
            )
            .select_related(
                "decision_conge",
                "decision_conge__evenement",
            )
            .prefetch_related(
                "mouvements",
                "mouvements__type_mouvement",
            )
            .order_by(
                "decision_conge__evenement__date_effet",
            )
        )

        for compteur in compteurs:

            if not compteur.est_solde:

                return compteur

        return None
    
    @property
    def occupation_courante(self):
        """
        Retourne l'occupation de poste en cours.
        """

        return (
            self.occupations_poste
            .select_related("poste")
            .filter(date_fin__isnull=True)
            .first()
        )

    @property
    def possede_compte(self):
        """
        Indique si l'agent possède
        un compte utilisateur.
        """

        return self.user is not None

    def clean(self):
        super().clean()

        statut = self.statut.code.upper()

        if statut in ("FONCTIONNAIRE", "DECISIONNAIRE") and not self.matricule:
            raise ValidationError(
                {
                    "matricule": (
                        "Le matricule est obligatoire pour un fonctionnaire "
                        "ou un décisionnaire."
                    )
                }
            )

        if statut == "CONTRACTUEL" and not self.numero_solde:
            raise ValidationError(
                {
                    "numero_solde": (
                        "Le numéro de solde est obligatoire pour un contractuel."
                    )
                }
            )

    def __str__(self):
        identifiant = self.matricule or self.numero_solde
        return f"{identifiant} - {self.nom} {self.prenom}"