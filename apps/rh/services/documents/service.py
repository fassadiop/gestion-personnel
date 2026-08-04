"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/documents/service.py

Description :
    Service métier du domaine documentaire.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.db.models import QuerySet

from apps.rh.models.documents import (
    DocumentAdministratif,
)


class DocumentService:
    """
    Service métier du domaine documentaire.

    Ce service centralise toutes les opérations
    fonctionnelles relatives aux documents
    administratifs.
    """

    @staticmethod
    def documents_agent(
        agent_id: int,
    ) -> QuerySet:
        """
        Retourne tous les documents administratifs
        d'un agent.
        """

        return (
            DocumentAdministratif.objects
            .filter(
                evenement__agent_id=agent_id,
                actif=True,
            )
            .select_related(
                "evenement",
                "evenement__agent",
                "type_document",
                "structure_emettrice",
            )
            .order_by(
                "-date_document",
                "-created_at",
            )
        )

    @staticmethod
    def documents_evenement(
        evenement_id: int,
    ) -> QuerySet:
        """
        Retourne les documents d'un événement.
        """

        return (
            DocumentAdministratif.objects
            .filter(
                evenement_id=evenement_id,
                actif=True,
            )
            .select_related(
                "type_document",
                "structure_emettrice",
            )
            .order_by(
                "-date_document",
                "-created_at",
            )
        )

    @staticmethod
    def remplacer_fichier(
        document: DocumentAdministratif,
        fichier,
    ) -> DocumentAdministratif:
        """
        Remplace le fichier d'un document.
        """

        document.fichier = fichier
        document.save()

        return document

    @staticmethod
    def supprimer(
        document: DocumentAdministratif,
    ) -> None:
        """
        Suppression logique d'un document.
        """

        document.actif = False

        document.save(
            update_fields=[
                "actif",
            ]
        )