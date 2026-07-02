# apps/rh/models/medical.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : apps/rh/models/medical.py

Description :
    Domaine médical.

    Ce module gère les informations médicales ayant une
    incidence sur la carrière administrative des agents.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.db import models

from apps.rh.core.base import BaseStructureModel

from apps.rh.models.base_evenement import BaseEvenementModel

from apps.rh.models.agent import Agent
from apps.rh.models.documents import DocumentAdministratif
from apps.rh.models.referentiels import TypeDocumentMedical


class DossierMedical(BaseStructureModel):
    """
    Dossier médical administratif d'un agent.

    Ce dossier centralise les informations médicales ayant
    une incidence sur la carrière administrative.

    Il est créé automatiquement lors du premier acte
    médical concernant l'agent.
    """

    agent = models.OneToOneField(
        Agent,
        on_delete=models.PROTECT,
        related_name="dossier_medical",
        verbose_name="Agent",
        help_text="Agent titulaire du dossier médical.",
    )

    numero_dossier = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="Numéro du dossier",
        help_text="Numéro unique généré automatiquement par le système.",
    )

    date_ouverture = models.DateField(
        verbose_name="Date d'ouverture",
        help_text="Date d'ouverture du dossier médical.",
    )

    observation = models.TextField(
        blank=True,
        default="",
        verbose_name="Observations",
        help_text="Observations générales relatives au dossier médical.",
    )

    class Meta:
        db_table = "rh_dossier_medical"

        verbose_name = "Dossier médical"
        verbose_name_plural = "Dossiers médicaux"

        ordering = [
            "agent__matricule",
        ]

        constraints = [

            models.UniqueConstraint(
                fields=["agent"],
                name="uq_dossier_medical_agent",
            ),

        ]

        indexes = [

            models.Index(fields=["agent"]),

        ]

    def __str__(self):
        return (
            f"{self.numero_dossier} - {self.agent}"
        )
    

class DocumentMedical(BaseEvenementModel):
    """
    Document médical produit par un professionnel de santé
    et ayant une incidence sur la carrière administrative
    d'un agent.

    Ce document constitue une pièce justificative versée au
    dossier médical de l'agent.

    Les informations communes (agent, acte administratif,
    dates d'effet, documents, etc.) sont portées par
    EvenementCarriere.
    """

    dossier_medical = models.ForeignKey(
        DossierMedical,
        on_delete=models.PROTECT,
        related_name="documents_medicaux",
        verbose_name="Dossier médical",
        help_text="Dossier médical auquel est rattaché le document.",
    )

    type_document = models.ForeignKey(
        TypeDocumentMedical,
        on_delete=models.PROTECT,
        related_name="documents_medicaux",
        verbose_name="Type de document médical",
        help_text="Nature du document médical.",
    )

    document_administratif = models.OneToOneField(
        DocumentAdministratif,
        on_delete=models.PROTECT,
        related_name="document_medical",
        verbose_name="Document administratif",
        help_text="Document administratif numérisé associé.",
    )

    nom_medecin = models.CharField(
        max_length=255,
        verbose_name="Nom du médecin",
        help_text="Nom du professionnel de santé signataire.",
    )

    qualite_medecin = models.CharField(
        max_length=150,
        blank=True,
        default="",
        verbose_name="Qualité du médecin",
        help_text="Qualité, spécialité ou fonction du signataire.",
    )

    structure_sanitaire = models.CharField(
        max_length=255,
        verbose_name="Structure sanitaire",
        help_text="Structure sanitaire ayant établi le document.",
    )

    date_emission = models.DateField(
        verbose_name="Date d'émission",
        help_text="Date d'établissement du document médical.",
    )

    date_reception = models.DateField(
        verbose_name="Date de réception",
        help_text="Date de réception du document par l'administration.",
    )

    date_debut_effet = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de début d'effet",
        help_text="Date de début des effets administratifs du document.",
    )

    date_fin_effet = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date de fin d'effet",
        help_text="Date de fin des effets administratifs du document.",
    )

    motif = models.CharField(
        max_length=255,
        blank=True,
        default="",
        verbose_name="Motif",
        help_text="Motif ou objet du document médical.",
    )

    acces_restreint = models.BooleanField(
        default=True,
        verbose_name="Accès restreint",
        help_text="Indique si le document est soumis à des restrictions d'accès.",
    )

    observation = models.TextField(
        blank=True,
        default="",
        verbose_name="Observations",
        help_text="Observations complémentaires.",
    )

    class Meta:
        db_table = "rh_document_medical"

        verbose_name = "Document médical"
        verbose_name_plural = "Documents médicaux"

        ordering = [
            "-date_emission",
            "-id",
        ]

        indexes = [

            models.Index(fields=["dossier_medical"]),

            models.Index(fields=["type_document"]),

            models.Index(fields=["date_emission"]),

            models.Index(fields=["date_reception"]),

            models.Index(fields=["date_debut_effet"]),

            models.Index(fields=["date_fin_effet"]),

        ]

        constraints = [

            models.CheckConstraint(
                condition=(
                    models.Q(date_debut_effet__isnull=True)
                    | models.Q(date_fin_effet__isnull=True)
                    | models.Q(
                        date_fin_effet__gte=models.F("date_debut_effet")
                    )
                ),
                name="ck_document_medical_periode",
            ),

        ]

    def __str__(self):
        return (
            f"{self.type_document.libelle} "
            f"({self.agent})"
        )