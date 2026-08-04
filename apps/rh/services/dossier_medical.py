# apps/rh/services/dossier_medical.py

from collections import defaultdict

from django.shortcuts import get_object_or_404

from apps.rh.models.agent import Agent
from apps.rh.models.documents import DocumentAdministratif
from apps.rh.models.evenement import EvenementCarriere


class DossierMedicalService:
    """
    Construit le dossier médical d'un agent.

    Le dossier est une projection métier composée de :
        - l'agent ;
        - un résumé médical ;
        - un historique médical.

    Chaque élément de l'historique regroupe :
        - un événement médical ;
        - les documents associés à cet événement.
    """

    TYPES_EVENEMENTS = (
        "CONGE_MALADIE",
        "CONGE_MATERNITE",
        "INAPTITUDE_MEDICALE",
        "RESTRICTION_MEDICALE",
        "ACCIDENT_TRAVAIL",
    )

    def __init__(self, agent_id):
        self.agent = get_object_or_404(Agent, pk=agent_id)

        self.evenements = list(
            EvenementCarriere.objects.filter(
                agent=self.agent,
                type_evenement__code__in=self.TYPES_EVENEMENTS,
                actif=True,
            )
            .select_related(
                "type_evenement",
                "statut",
                "position_administrative",
            )
            .order_by("-date_effet")
        )

        self.documents = list(
            DocumentAdministratif.objects.filter(
                evenement__in=self.evenements
            )
            .select_related(
                "type_document",
                "structure_emettrice",
                "evenement",
            )
            .order_by("-date_document")
        )

    def _documents_par_evenement(self):
        """
        Indexe les documents par événement.
        """
        documents = defaultdict(list)

        for document in self.documents:
            documents[document.evenement_id].append(document)

        return documents

    def get_resume(self):
        """
        Construit le résumé médical.
        """

        resume = {
            "nombre_evenements": len(self.evenements),
            "nombre_documents": len(self.documents),

            "dernier_conge_maladie": None,
            "derniere_restriction": None,
            "derniere_inaptitude": None,
            "dernier_accident": None,

            "etat_medical": {
                "statut": "NORMAL",
                "evenement": None,
            },
        }

        for evenement in self.evenements:

            code = evenement.type_evenement.code

            if (
                code == "CONGE_MALADIE"
                and resume["dernier_conge_maladie"] is None
            ):
                resume["dernier_conge_maladie"] = evenement

            elif (
                code == "RESTRICTION_MEDICALE"
                and resume["derniere_restriction"] is None
            ):
                resume["derniere_restriction"] = evenement

            elif (
                code == "INAPTITUDE_MEDICALE"
                and resume["derniere_inaptitude"] is None
            ):
                resume["derniere_inaptitude"] = evenement

            elif (
                code == "ACCIDENT_TRAVAIL"
                and resume["dernier_accident"] is None
            ):
                resume["dernier_accident"] = evenement

        # Détermination de l'état médical courant
        if resume["derniere_inaptitude"] is not None:
            resume["etat_medical"] = {
                "statut": "INAPTITUDE_ACTIVE",
                "evenement": resume["derniere_inaptitude"],
            }

        elif resume["derniere_restriction"] is not None:
            resume["etat_medical"] = {
                "statut": "RESTRICTION_ACTIVE",
                "evenement": resume["derniere_restriction"],
            }

        return resume

    def get_historique(self):
        """
        Construit l'historique médical.

        Chaque élément contient :
            - un événement médical ;
            - les documents qui le justifient.
        """

        documents = self._documents_par_evenement()

        historique = []

        for evenement in self.evenements:
            historique.append(
                {
                    "evenement": evenement,
                    "documents": documents.get(evenement.id, []),
                }
            )

        return historique

    def get_dossier(self):
        """
        Retourne le dossier médical complet.
        """

        return {
            "agent": self.agent,
            "resume": self.get_resume(),
            "historique": self.get_historique(),
        }