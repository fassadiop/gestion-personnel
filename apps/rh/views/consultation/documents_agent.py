from datetime import timedelta

from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.rh.constants.evenements import EVENEMENTS_MEDICAUX
from apps.rh.models.documents import (
    DocumentAdministratif,
    DocumentAgent,
)

class DocumentsAgentView(APIView):
    """
    Vue consolidée du dossier documentaire d'un agent.

    Regroupe :
    - les documents personnels de l'agent ;
    - les documents administratifs liés à ses événements
      de carrière ;
    - les indicateurs de synthèse du dossier documentaire.
    """

    def get(self, request, agent_id):
        aujourd_hui = timezone.localdate()

        limite_expiration = (
            aujourd_hui + timedelta(days=90)
        )

        # ======================================================
        # DOCUMENTS PERSONNELS
        # ======================================================

        documents_personnels = (
            DocumentAgent.objects
            .filter(
                agent_id=agent_id,
                actif=True,
            )
            .select_related(
                "type_document",
                "verifie_par",
            )
            .order_by(
                "type_document__libelle",
                "-date_document",
            )
        )

        # ======================================================
        # DOCUMENTS ADMINISTRATIFS
        # ======================================================

        documents_administratifs = (
            DocumentAdministratif.objects
            .filter(
                evenement__agent_id=agent_id,
                actif=True,
            )
            .exclude(
                evenement__type_evenement__code__in=EVENEMENTS_MEDICAUX,
            )
            .select_related(
                "evenement",
                "type_document",
                "structure_emettrice",
            )
            .order_by(
                "-date_document",
                "-id",
            )
        )

        # ======================================================
        # PROJECTION DOCUMENTS PERSONNELS
        # ======================================================

        personnels = []

        for document in documents_personnels:
            est_expire = (
                document.date_expiration is not None
                and document.date_expiration < aujourd_hui
            )

            expire_bientot = (
                document.date_expiration is not None
                and aujourd_hui
                <= document.date_expiration
                <= limite_expiration
            )

            personnels.append(
                {
                    "id": document.id,

                    "type_document": {
                        "id": document.type_document.id,
                        "code": document.type_document.code,
                        "libelle": document.type_document.libelle,
                    },

                    "numero_document":
                        document.numero_document,

                    "date_document":
                        document.date_document,

                    "date_expiration":
                        document.date_expiration,

                    "fichier":
                        request.build_absolute_uri(
                            document.fichier.url
                        )
                        if document.fichier
                        else None,

                    "nom_fichier":
                        document.nom_fichier,

                    "extension":
                        document.extension,

                    "taille":
                        document.taille,

                    "mime_type":
                        document.mime_type,

                    "description":
                        document.description,

                    "est_verifie":
                        document.est_verifie,

                    "date_verification":
                        document.date_verification,

                    "est_expire":
                        est_expire,

                    "expire_bientot":
                        expire_bientot,
                }
            )

        # ======================================================
        # PROJECTION DOCUMENTS ADMINISTRATIFS
        # ======================================================

        administratifs = []

        for document in documents_administratifs:
            administratifs.append(
                {
                    "id": document.id,

                    "type_document": {
                        "id": document.type_document.id,
                        "code": document.type_document.code,
                        "libelle": document.type_document.libelle,
                    },

                    "numero_document":
                        document.numero_document,

                    "date_document":
                        document.date_document,

                    "signataire":
                        document.signataire,

                    "structure_emettrice": {
                        "id": document.structure_emettrice.id,
                        "nom": document.structure_emettrice.nom,
                    },

                    "evenement": {
                        "id":
                            document.evenement.id,
                        "date_effet":
                            document.evenement.date_effet,
                    },

                    "fichier":
                        request.build_absolute_uri(
                            document.fichier.url
                        )
                        if document.fichier
                        else None,

                    "nom_fichier":
                        document.nom_fichier,

                    "extension":
                        document.extension,

                    "taille":
                        document.taille,

                    "mime_type":
                        document.mime_type,

                    "description":
                        document.description,
                }
            )

        # ======================================================
        # SYNTHÈSE
        # ======================================================

        documents_a_verifier = sum(
            1
            for document in personnels
            if not document["est_verifie"]
        )

        documents_expires = sum(
            1
            for document in personnels
            if document["est_expire"]
        )

        documents_expirant_bientot = sum(
            1
            for document in personnels
            if document["expire_bientot"]
        )

        return Response(
            {
                "agent_id": agent_id,

                "synthese": {
                    "total_documents":
                        len(personnels)
                        + len(administratifs),

                    "documents_personnels":
                        len(personnels),

                    "documents_administratifs":
                        len(administratifs),

                    "documents_a_verifier":
                        documents_a_verifier,

                    "documents_expires":
                        documents_expires,

                    "documents_expirant_bientot":
                        documents_expirant_bientot,
                },

                "documents_personnels":
                    personnels,

                "documents_administratifs":
                    administratifs,
            }
        )