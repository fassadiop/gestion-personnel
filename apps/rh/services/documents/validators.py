"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/documents/validators.py

Description :
    Validations métier du domaine documentaire.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.core.exceptions import ValidationError

from apps.rh.models.documents import (
    DocumentAdministratif,
)


class DocumentValidator:
    """
    Validateur métier des documents administratifs.
    """

    @staticmethod
    def verifier_document_actif(
        document: DocumentAdministratif,
    ) -> None:
        """
        Vérifie que le document est actif.
        """

        if not document.actif:
            raise ValidationError(
                "Ce document est inactif."
            )

    @staticmethod
    def verifier_fichier(
        document: DocumentAdministratif,
    ) -> None:
        """
        Vérifie qu'un fichier est associé au document.
        """

        if not document.fichier:
            raise ValidationError(
                "Aucun fichier n'est associé à ce document."
            )

    @staticmethod
    def verifier_evenement(
        document: DocumentAdministratif,
    ) -> None:
        """
        Vérifie que le document est rattaché
        à un événement.
        """

        if document.evenement is None:
            raise ValidationError(
                "Le document doit être rattaché à un événement."
            )