# apps/rh/models/organisation.py

from django.db import models

from apps.rh.core.base import (
    BaseLibelleModel,
    BaseStructureModel,
)

class TypeStructure(BaseLibelleModel):
    """
    Type de structure administrative.

    Exemples :
    - Ministère
    - Direction
    - Agence
    - Projet
    - Programme
    - Etablissement public
    """

    class Meta:
        db_table = "rh_type_structure"
        verbose_name = "Type de structure"
        verbose_name_plural = "Types de structures"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class TypeUniteOrganisationnelle(BaseLibelleModel):
    """
    Type d'unité organisationnelle.

    Exemples :
    - Direction
    - Division
    - Service
    - Bureau
    - Cellule
    - Centre
    - Antenne
    """

    class Meta:
        db_table = "rh_type_unite_organisationnelle"
        verbose_name = "Type d'unité organisationnelle"
        verbose_name_plural = "Types d'unités organisationnelles"

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]


class Structure(BaseStructureModel):
    """
    Structure administrative autonome.

    Une structure représente une organisation disposant
    de son propre organigramme et de son autonomie
    administrative.

    Exemples :

    - Ministère
    - Agence nationale
    - Établissement public
    - Projet
    - Programme
    """

    type_structure = models.ForeignKey(
        TypeStructure,
        on_delete=models.PROTECT,
        related_name="structures",
        verbose_name="Type de structure",
        help_text="Type de la structure.",
    )

    code = models.CharField(
        max_length=30,
        verbose_name="Code",
        help_text="Code unique de la structure.",
    )

    sigle = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Sigle",
        help_text="Sigle officiel de la structure.",
    )

    nom = models.CharField(
        max_length=255,
        verbose_name="Nom",
        help_text="Nom officiel de la structure.",
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

    site_web = models.URLField(
        blank=True,
        verbose_name="Site web",
    )

    date_creation = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de création",
        help_text="Date officielle de création de la structure.",
    )

    class Meta:
        db_table = "rh_structure"
        verbose_name = "Structure"
        verbose_name_plural = "Structures"
        ordering = ["nom"]

        constraints = [
            models.UniqueConstraint(
                fields=["code"],
                name="uq_structure_code",
            ),
            models.UniqueConstraint(
                fields=["nom"],
                name="uq_structure_nom",
            ),
        ]

        indexes = [
            models.Index(fields=["code"]),
            models.Index(fields=["nom"]),
            models.Index(fields=["sigle"]),
        ]

    def __str__(self):
        return f"{self.sigle} - {self.nom}"
    

class UniteOrganisationnelle(BaseStructureModel):
    """
    Unité organisationnelle appartenant à une structure.

    Une unité organisationnelle représente un niveau de
    l'organigramme (Direction, Division, Bureau, Service,
    Cellule, Centre, etc.).
    """

    type_unite = models.ForeignKey(
        TypeUniteOrganisationnelle,
        on_delete=models.PROTECT,
        related_name="unites",
        verbose_name="Type d'unité",
        help_text="Type de l'unité organisationnelle.",
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="enfants",
        verbose_name="Unité parente",
        help_text="Unité immédiatement supérieure.",
    )

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="unites",
        verbose_name="Structure",
        help_text="Structure de rattachement.",
    )

    code = models.CharField(
        max_length=30,
        verbose_name="Code",
        help_text="Code de l'unité.",
    )

    sigle = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Sigle",
        help_text="Sigle de l'unité.",
    )

    nom = models.CharField(
        max_length=255,
        verbose_name="Nom",
        help_text="Nom de l'unité organisationnelle.",
    )

    responsable = models.ForeignKey(
        "Agent",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="unites_dirigees",
        verbose_name="Responsable",
        help_text="Agent responsable de l'unité organisationnelle.",
    )

    ordre = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Ordre",
        help_text="Ordre d'affichage dans l'organigramme.",
    )

    class Meta:
        db_table = "rh_unite_organisationnelle"
        verbose_name = "Unité organisationnelle"
        verbose_name_plural = "Unités organisationnelles"
        ordering = ["ordre", "nom"]

        constraints = [
            models.UniqueConstraint(
                fields=["structure", "code"],
                name="uq_unite_structure_code",
            ),
            models.UniqueConstraint(
                fields=["structure", "nom"],
                name="uq_unite_structure_nom",
            ),
        ]

        indexes = [
            models.Index(fields=["structure"]),
            models.Index(fields=["parent"]),
            models.Index(fields=["type_unite"]),
            models.Index(fields=["code"]),
            models.Index(fields=["nom"]),
        ]

    def __str__(self):
        return self.nom
    

class Poste(BaseStructureModel):
    """
    Poste appartenant à une unité organisationnelle.

    Un poste existe indépendamment de l'agent qui l'occupe.
    """

    structure = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="postes",
        verbose_name="Structure",
        help_text="Structure de rattachement.",
    )

    unite = models.ForeignKey(
        UniteOrganisationnelle,
        on_delete=models.PROTECT,
        related_name="postes",
        verbose_name="Unité organisationnelle",
        help_text="Unité organisationnelle de rattachement.",
    )

    code = models.CharField(
        max_length=30,
        verbose_name="Code",
        help_text="Code du poste.",
    )

    libelle = models.CharField(
        max_length=255,
        verbose_name="Libellé",
        help_text="Libellé du poste.",
    )

    description = models.TextField(
        blank=True,
        default="",
        verbose_name="Description",
        help_text="Description des missions du poste.",
    )

    hierarchie_minimale = models.ForeignKey(
        "Hierarchie",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="postes",
        verbose_name="Hiérarchie minimale",
        help_text="Hiérarchie minimale requise pour occuper ce poste.",
    )

    est_responsable = models.BooleanField(
        default=False,
        verbose_name="Poste de responsabilité",
        help_text="Indique si ce poste est responsable de l'unité.",
    )

    est_budgetise = models.BooleanField(
        default=True,
        verbose_name="Poste budgétisé",
        help_text="Indique si le poste est prévu dans l'organigramme officiel."
    )

    class Meta:
        db_table = "rh_poste"
        verbose_name = "Poste"
        verbose_name_plural = "Postes"
        ordering = ["libelle"]

        constraints = [
            models.UniqueConstraint(
                fields=["structure", "code"],
                name="uq_poste_structure_code",
            ),
            models.UniqueConstraint(
                fields=["unite", "libelle"],
                name="uq_poste_unite_libelle",
            ),
        ]

        indexes = [
            models.Index(fields=["structure"]),
            models.Index(fields=["unite"]),
            models.Index(fields=["code"]),
            models.Index(fields=["libelle"]),
        ]

    def __str__(self):
        return self.libelle