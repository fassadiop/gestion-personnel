"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : core/base.py

Description :
    Classes abstraites de base utilisées par tous les
    modèles du projet.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from __future__ import annotations
from django.db import models

from django.db.models import F, Q


class BaseModel(models.Model):
    """
    Classe abstraite de base héritée par toutes les entités.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création",
        help_text="Date de création de l'enregistrement.",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Date de modification",
        help_text="Date de la dernière modification.",
    )

    observation = models.TextField(
        blank=True,
        default="",
        verbose_name="Observation",
        help_text="Observation libre.",
    )

    actif = models.BooleanField(
        default=True,
        verbose_name="Actif",
        help_text="Indique si l'enregistrement est actif.",
    )

    class Meta:
        abstract = True


class BaseDocument(BaseModel):
    """
    Classe abstraite de base pour tous les documents du SGCP.

    Cette classe centralise les informations techniques
    communes à tous les documents numériques du système.

    Elle ne contient aucune information métier.

    Les modèles DocumentAdministratif et DocumentAgent
    héritent de cette classe.
    """

    fichier = models.FileField(
        upload_to="documents/%Y/%m/",
        verbose_name="Fichier",
    )

    nom_fichier = models.CharField(
        max_length=255,
        editable=False,
        verbose_name="Nom du fichier",
    )

    extension = models.CharField(
        max_length=10,
        editable=False,
        verbose_name="Extension",
    )

    taille = models.PositiveBigIntegerField(
        default=0,
        editable=False,
        verbose_name="Taille (octets)",
    )

    mime_type = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Type MIME",
    )

    hash_document = models.CharField(
        max_length=64,
        blank=True,
        editable=False,
        verbose_name="Empreinte SHA-256",
    )

    texte_ocr = models.TextField(
        blank=True,
        verbose_name="Texte OCR",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )

    class Meta:
        abstract = True

    @property
    def nom_complet(self):
        """
        Retourne le nom complet du document.
        """
        return f"{self.nom_fichier}{self.extension}"


class BaseReferentielModel(BaseModel):
    """
    Classe abstraite de base des référentiels RH.
    """

    class Meta:
        abstract = True


class BaseStructureModel(BaseModel):
    """
    Classe abstraite de base des entités
    rattachées à une structure.
    """

    class Meta:
        abstract = True


class BasePeriodeModel(BaseStructureModel):
    """
    Classe abstraite de base des entités
    possédant une période de validité.
    """

    date_debut = models.DateField(
        verbose_name="Date de début",
        help_text="Date de début de validité.",
    )

    date_fin = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de fin",
        help_text="Date de fin de validité.",
    )

    class Meta:
        abstract = True
        constraints = [
            models.CheckConstraint(
                condition=Q(date_fin__isnull=True) | Q(date_fin__gte=F("date_debut")),
                name="ck_date_fin",
            ),
        ]


class BaseDecisionModel(BaseStructureModel):
    """
    Classe abstraite de base des décisions administratives.
    """

    numero_decision = models.CharField(
        max_length=100,
        verbose_name="Numéro de décision",
        help_text="Numéro officiel de la décision.",
    )

    date_signature = models.DateField(
        verbose_name="Date de signature",
        help_text="Date de signature de la décision.",
    )

    autorite_signataire = models.CharField(
        max_length=255,
        verbose_name="Autorité signataire",
        help_text="Autorité ayant signé la décision.",
    )

    class Meta:
        abstract = True


class BaseLibelleModel(BaseReferentielModel):
    """
    Classe abstraite de base des référentiels
    simples composés d'un code, d'un libellé
    et d'une description.
    """

    code = models.CharField(
        max_length=30,
        verbose_name="Code",
        help_text="Code unique du référentiel.",
    )

    libelle = models.CharField(
        max_length=255,
        verbose_name="Libellé",
        help_text="Libellé du référentiel.",
    )

    description = models.TextField(
        blank=True,
        default="",
        verbose_name="Description",
        help_text="Description du référentiel.",
    )

    class Meta:
        abstract = True
        ordering = ["libelle"]

    def __str__(self):
        return f"{self.code} - {self.libelle}"


__all__ = [
    "BaseModel",
    "BaseReferentielModel",
    "BaseLibelleModel",
    "BaseStructureModel",
    "BasePeriodeModel",
    "BaseDecisionModel",
]


