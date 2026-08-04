from rest_framework.response import Response
from rest_framework.views import APIView

from apps.rh.models.absence import Absence


class AbsencesAgentView(APIView):
    """
    Vue consolidée des absences d'un agent.

    Fournit l'historique des autorisations d'absence
    ainsi que leur éventuel impact sur les droits
    à congé.
    """

    def get(self, request, agent_id):
        absences = (
            Absence.objects
            .filter(
                evenement__agent_id=agent_id,
                actif=True,
            )
            .select_related(
                "type_absence",
                "evenement",
            )
            .order_by(
                "-date_debut",
                "-id",
            )
        )

        resultats = [
            {
                "id": absence.id,
                "type_absence": {
                    "id": absence.type_absence.id,
                    "code": absence.type_absence.code,
                    "libelle": absence.type_absence.libelle,
                },
                "date_debut": absence.date_debut,
                "date_fin": absence.date_fin,
                "nombre_jours": absence.nombre_jours,
                "jours_deductibles": absence.jours_deductibles,
                "motif": absence.motif,
                "date_effet": absence.evenement.date_effet,
            }
            for absence in absences
        ]

        return Response(
            {
                "agent_id": agent_id,
                "nombre_absences": len(resultats),
                "total_jours_absence": sum(
                    absence["nombre_jours"]
                    for absence in resultats
                ),
                "total_jours_deductibles": sum(
                    absence["jours_deductibles"]
                    for absence in resultats
                ),
                "absences": resultats,
            }
        )