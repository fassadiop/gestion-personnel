# apps/rh/models/referentiels.py

from django.db import models

from apps.rh.core.base import (
    BaseLibelleModel,
)

class Hierarchie(BaseLibelleModel):
    """
    Hiérarchie de la Fonction Publique.

    Exemples :
    - A
    - A2
    - B
    - C
    - D
    """
    
    abreviation = models.CharField(
        max_length=10,
        verbose_name="Abréviation",
        help_text="Abréviation officielle de la hiérarchie.",
    )

    ordre = models.PositiveSmallIntegerField(
        verbose_name="Ordre",
        help_text="Ordre de la hiérarchie (1 = plus élevée).",
    )

    class Meta:
        db_table = "rh_hierarchie"
        verbose_name = "Hiérarchie"
        verbose_name_plural = "Hiérarchies"
        ordering = ["ordre"]

        constraints = [
            models.UniqueConstraint(
                fields=["ordre"],
                name="uq_hierarchie_ordre",
            ),
        ]

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
            models.Index(fields=["ordre"]),
        ]


class Corps(BaseLibelleModel):
    """
    Corps de la Fonction Publique.
    """

    hierarchie = models.ForeignKey(
        Hierarchie,
        on_delete=models.PROTECT,
        related_name="corps",
        verbose_name="Hiérarchie",
        help_text="Hiérarchie à laquelle appartient le corps.",
    )

    class Meta:
        db_table = "rh_corps"
        verbose_name = "Corps"
        verbose_name_plural = "Corps"
        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
            models.Index(fields=["hierarchie"]),
        ]


class Grade(BaseLibelleModel):
    """
    Grade appartenant à un corps.
    """

    corps = models.ForeignKey(
        "Corps",
        on_delete=models.PROTECT,
        related_name="grades",
        verbose_name="Corps",
        help_text="Corps auquel appartient le grade.",
    )

    class Meta:
        db_table = "rh_grade"
        verbose_name = "Grade"
        verbose_name_plural = "Grades"
        ordering = ["corps__libelle", "libelle"]


        constraints = [
            models.UniqueConstraint(
                fields=["corps", "code"],
                name="uq_grade_corps_code",
            ),
            models.UniqueConstraint(
                fields=["corps", "libelle"],
                name="uq_grade_corps_libelle",
            ),
        ]
        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
            models.Index(fields=["corps"]),
        ]


class Classe(BaseLibelleModel):
    """
    Classe appartenant à un grade.
    """

    grade = models.ForeignKey(
        "Grade",
        on_delete=models.PROTECT,
        related_name="classes",
        verbose_name="Grade",
        help_text="Grade auquel appartient la classe.",
    )

    ordre = models.PositiveSmallIntegerField(
        verbose_name="Ordre",
        help_text="Ordre de la classe dans le grade.",
    )

    indice_min = models.PositiveIntegerField(
        verbose_name="Indice minimum",
        help_text="Indice minimum de la classe.",
    )

    indice_max = models.PositiveIntegerField(
        verbose_name="Indice maximum",
        help_text="Indice maximum de la classe.",
    )

    class Meta:
        db_table = "rh_classe"
        verbose_name = "Classe"
        verbose_name_plural = "Classes"
        ordering = ["grade", "ordre"]

        constraints = [
            models.UniqueConstraint(
                fields=["grade", "ordre"],
                name="uq_classe_grade_ordre",
            ),
            models.UniqueConstraint(
                fields=["grade", "code"],
                name="uq_classe_grade_code",
            ),
            models.CheckConstraint(
                condition=models.Q(indice_min__lte=models.F("indice_max")),
                name="ck_classe_indice",
            ),
            models.UniqueConstraint(
                fields=["grade", "libelle"],
                name="uq_classe_grade_libelle",
            ),
        ]
        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
            models.Index(fields=["grade"]),
        ]
    

class Echelon(BaseLibelleModel):
    """
    Échelon appartenant à une classe.
    """

    classe = models.ForeignKey(
        "Classe",
        on_delete=models.PROTECT,
        related_name="echelons",
        verbose_name="Classe",
        help_text="Classe à laquelle appartient l'échelon.",
    )

    ordre = models.PositiveSmallIntegerField(
        verbose_name="Ordre",
    )

    indice = models.PositiveIntegerField(
        verbose_name="Indice",
        help_text="Indice correspondant à l'échelon.",
    )

    class Meta:
        db_table = "rh_echelon"
        verbose_name = "Échelon"
        verbose_name_plural = "Échelons"
        ordering = ["classe", "ordre"]

        constraints = [
            models.UniqueConstraint(
                fields=["classe", "ordre"],
                name="uq_echelon_classe_ordre",
            ),
            models.UniqueConstraint(
                fields=["classe", "code"],
                name="uq_echelon_classe_code",
            ),
            models.UniqueConstraint(
                fields=["classe", "libelle"],
                name="uq_echelon_classe_libelle",
            ),
        ]
        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
            models.Index(fields=["classe"]),
        ]
    

# ==========================================================
# Référentiels administratifs
# ==========================================================


class PositionAdministrative(BaseLibelleModel):
    """
    Position administrative d'un agent.

    Exemples :
    - En activité
    - Détachement
    - Disponibilité
    - Suspension
    - Retraite
    """

    class Meta:
        db_table = "rh_position_administrative"
        verbose_name = "Position administrative"
        verbose_name_plural = "Positions administratives"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class TypeEvenement(BaseLibelleModel):
    """
    Type d'événement de carrière.

    Exemples :
    - Recrutement
    - Affectation
    - Mutation
    - Promotion
    - Avancement
    - Formation
    - Mission
    - Congé
    - Retraite
    """

    class Meta:
        db_table = "type_evenement_carriere"
        verbose_name = "Type d'événement de carrière"
        verbose_name_plural = "Types d'événements de carrière"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class TypeDocument(BaseLibelleModel):
    """
    Type de document administratif.
    """

    class Meta:
        db_table = "rh_type_document"
        verbose_name = "Type de document"
        verbose_name_plural = "Types de documents"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


# ==========================================================
# Référentiels RH
# ==========================================================


class TypeConge(BaseLibelleModel):
    """
    Référentiel des types de congé administratif.

    Ce référentiel décrit les caractéristiques
    permanentes d'un type de congé utilisées
    par le moteur de carrière.
    """

    duree_par_defaut = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Durée par défaut (jours)",
        help_text=(
            "Durée proposée automatiquement lors de la création "
            "d'une décision de congé."
        ),
    )

    fractionnement_autorise = models.BooleanField(
        default=False,
        verbose_name="Fractionnement autorisé",
        help_text=(
            "Indique si le congé peut être consommé "
            "en plusieurs périodes de jouissance."
        ),
    )

    justificatif_obligatoire = models.BooleanField(
        default=False,
        verbose_name="Justificatif obligatoire",
        help_text=(
            "Indique si une pièce justificative est "
            "obligatoire pour accorder ce type de congé."
        ),
    )

    impacte_compteur = models.BooleanField(
        default=True,
        verbose_name="Impacte le compteur",
        help_text=(
            "Indique si ce type de congé est déduit "
            "du compteur de congés de l'agent."
        ),
    )

    class Meta:
        verbose_name = "Type de congé"
        verbose_name_plural = "Types de congé"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class TypeAbsence(BaseLibelleModel):
    """
    Types d'absences.
    """

    class Meta:
        db_table = "rh_type_absence"
        verbose_name = "Type d'absence"
        verbose_name_plural = "Types d'absences"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class TypeMouvementConge(
    BaseLibelleModel,
):
    """
    Référentiel des types de mouvements
    applicables au compteur de congé.

    Chaque mouvement représente une opération
    métier affectant le compteur de congé.
    """

    sens = models.SmallIntegerField(
        choices=(
            (1, "Crédit"),
            (-1, "Débit"),
        ),
        verbose_name="Sens",
        help_text=(
            "Sens du mouvement sur le compteur "
            "de congé."
        ),
    )

    class Meta:
        db_table = "rh_type_mouvement_conge"

        verbose_name = (
            "Type de mouvement de congé"
        )

        verbose_name_plural = (
            "Types de mouvements de congé"
        )

        ordering = (
            "libelle",
        )

        constraints = (
            models.CheckConstraint(
                condition=models.Q(
                    sens__in=(-1, 1)
                ),
                name=(
                    "ck_type_mouvement_conge_sens"
                ),
            ),
        )

        indexes = (
            models.Index(fields=("code",)),
            models.Index(fields=("libelle",)),
            models.Index(fields=("sens",)),
        )

    def __str__(self):
        return self.libelle


class TypeSanction(BaseLibelleModel):
    """
    Référentiel des types de sanctions disciplinaires.
    """

    class Meta:
        db_table = "rh_type_sanction"

        verbose_name = "Type de sanction"
        verbose_name_plural = "Types de sanctions"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class TypeDecoration(BaseLibelleModel):
    """
    Types de décorations.
    """

    class Meta:
        db_table = "rh_type_decoration"
        verbose_name = "Type de décoration"
        verbose_name_plural = "Types de décorations"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


# ==========================================================
# Référentiels Formation
# ==========================================================


class TypeFormation(BaseLibelleModel):
    """
    Types de formation.
    """

    class Meta:
        db_table = "rh_type_formation"
        verbose_name = "Type de formation"
        verbose_name_plural = "Types de formations"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class NiveauFormation(BaseLibelleModel):
    """
    Niveaux de formation.
    """

    class Meta:
        db_table = "rh_niveau_formation"
        verbose_name = "Niveau de formation"
        verbose_name_plural = "Niveaux de formation"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


# ==========================================================
# Référentiels Compétences
# ==========================================================


class TypeCompetence(BaseLibelleModel):
    """
    Types de compétences.
    """

    class Meta:
        db_table = "rh_type_competence"
        verbose_name = "Type de compétence"
        verbose_name_plural = "Types de compétences"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


# ==========================================================
# Référentiels Missions
# ==========================================================


class TypeMission(BaseLibelleModel):
    """
    Types de missions.
    """

    class Meta:
        db_table = "rh_type_mission"
        verbose_name = "Type de mission"
        verbose_name_plural = "Types de missions"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


# ==========================================================
# Référentiels Agent
# ==========================================================


class Nationalite(BaseLibelleModel):
    """
    Nationalité d'un agent.
    """

    class Meta:
        db_table = "rh_nationalite"
        verbose_name = "Nationalité"
        verbose_name_plural = "Nationalités"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class EtatCivil(BaseLibelleModel):
    """
    État civil d'un agent.

    Exemples :
    - Célibataire
    - Marié(e)
    - Divorcé(e)
    - Veuf(ve)
    """

    class Meta:
        db_table = "rh_etat_civil"
        verbose_name = "État civil"
        verbose_name_plural = "États civils"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class StatutAgent(BaseLibelleModel):
    """
    Statut juridique de l'agent.

    Exemples :
    - Fonctionnaire
    - Contractuel
    - Décisionnaire
    - Stagiaire
    - Vacataire
    """

    class Meta:
        db_table = "rh_statut_agent"
        verbose_name = "Statut de l'agent"
        verbose_name_plural = "Statuts des agents"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class Sexe(BaseLibelleModel):
    """
    Sexe.

    Exemples :
    - Masculin
    - Féminin
    """

    class Meta:
        db_table = "rh_sexe"
        verbose_name = "Sexe"
        verbose_name_plural = "Sexes"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


# ==========================================================
# Référentiels Événements de carrière
# ==========================================================

class StatutEvenement(BaseLibelleModel):
    """
    Statut d'un événement de carrière.

    Exemples :
    - Brouillon
    - En attente
    - Validé
    - Refusé
    - Annulé
    """

    class Meta:
        db_table = "rh_statut_evenement"
        verbose_name = "Statut d'événement"
        verbose_name_plural = "Statuts d'événements"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


# ==========================================================
# Référentiels Formation
# ==========================================================

class Pays(BaseLibelleModel):
    """
    Pays.

    Référentiel partagé utilisé par plusieurs modules :
    - Formation
    - Mission
    - Coopération internationale
    """

    code_iso2 = models.CharField(
        max_length=2,
        unique=True,
        verbose_name="Code ISO 2",
        help_text="Code ISO 3166-1 alpha-2 (SN, FR, CA...).",
    )

    code_iso3 = models.CharField(
        max_length=3,
        unique=True,
        verbose_name="Code ISO 3",
        help_text="Code ISO 3166-1 alpha-3 (SEN, FRA, CAN...).",
    )

    class Meta:
        db_table = "rh_pays"
        verbose_name = "Pays"
        verbose_name_plural = "Pays"
        ordering = ["libelle"]

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class OrganismeFormation(BaseLibelleModel):
    """
    Organisme dispensant une formation.
    """

    pays = models.ForeignKey(
        Pays,
        on_delete=models.PROTECT,
        related_name="organismes_formation",
        verbose_name="Pays",
    )

    class Meta:
        db_table = "rh_organisme_formation"
        verbose_name = "Organisme de formation"
        verbose_name_plural = "Organismes de formation"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
            models.Index(fields=["pays"]),
        ]


class SourceFinancement(BaseLibelleModel):
    """
    Source de financement d'une formation ou d'une mission.

    Exemples :
    - État
    - Budget Ministère
    - Banque Mondiale
    - FAO
    - Coopération Japonaise
    - Personnel
    """

    class Meta:
        db_table = "rh_source_financement"
        verbose_name = "Source de financement"
        verbose_name_plural = "Sources de financement"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class NiveauCompetence(BaseLibelleModel):
    """
    Niveau de maîtrise d'une compétence.

    Exemples :
    - Débutant
    - Intermédiaire
    - Avancé
    - Expert
    """

    class Meta:
        db_table = "rh_niveau_competence"
        verbose_name = "Niveau de compétence"
        verbose_name_plural = "Niveaux de compétence"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


# ==========================================================
# Référentiels Médical
# ==========================================================

class TypeDocumentMedical(BaseLibelleModel):
    """
    Référentiel des types de documents médicaux.

    Ce référentiel permet de classifier les documents
    médicaux ayant une incidence sur la carrière
    administrative des agents.
    """

    class Meta:
        db_table = "ref_type_document_medical"

        verbose_name = "Type de document médical"
        verbose_name_plural = "Types de documents médicaux"

        ordering = [
            "libelle",
        ]


class TypeInaptitudeMedicale(BaseLibelleModel):
    """
    Référentiel des types d'inaptitude médicale.

    Ce référentiel permet de classifier les
    décisions administratives d'inaptitude
    ayant une incidence sur la carrière.
    """

    class Meta:
        db_table = "rh_type_inaptitude_medicale"

        verbose_name = (
            "Type d'inaptitude médicale"
        )

        verbose_name_plural = (
            "Types d'inaptitude médicale"
        )

        ordering = [
            "libelle",
        ]

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]