from rest_framework.response import Response
from rest_framework.views import APIView

from apps.rh.models.decision_conge import DecisionConge


class CongesAgentView(APIView):
    """
    Vue consolidée des congés d'un agent.

    Fournit :
    - les décisions de congé ;
    - l'état du compteur associé ;
    - les périodes effectives de jouissance ;
    - les mouvements du compteur.
    """

    def get(self, request, agent_id):
        decisions = (
            DecisionConge.objects
            .filter(
                evenement__agent_id=agent_id,
                actif=True,
            )
            .select_related(
                "type_conge",
                "evenement",
                "compteur",
            )
            .prefetch_related(
                "conges",
                "compteur__mouvements__type_mouvement",
            )
            .order_by("-evenement__date_effet")
        )

        resultats = []

        for decision in decisions:
            compteur = getattr(
                decision,
                "compteur",
                None,
            )

            conges = [
                {
                    "id": conge.id,
                    "date_cessation_service":
                        conge.date_cessation_service,
                    "date_reprise":
                        conge.date_reprise,
                    "nombre_jours":
                        conge.nombre_jours,
                    "numero_tranche":
                        conge.numero_tranche,
                    "est_fractionnement":
                        conge.est_fractionnement,
                }
                for conge in decision.conges.filter(
                    actif=True
                )
            ]

            mouvements = []

            if compteur:
                mouvements = [
                    {
                        "id": mouvement.id,
                        "type_mouvement":
                            mouvement.type_mouvement.libelle,
                        "sens":
                            mouvement.sens,
                        "nombre_jours":
                            mouvement.nombre_jours,
                        "impact":
                            mouvement.impact,
                        "date_mouvement":
                            mouvement.date_mouvement,
                        "observation":
                            mouvement.observation,
                    }
                    for mouvement
                    in compteur.mouvements.filter(
                        actif=True
                    )
                ]

            resultats.append(
                {
                    "id": decision.id,
                    "type_conge": {
                        "id": decision.type_conge.id,
                        "code": decision.type_conge.code,
                        "libelle":
                            decision.type_conge.libelle,
                    },
                    "date_decision":
                        decision.date_decision,
                    "date_effet":
                        decision.date_effet,
                    "nombre_jours_accordes":
                        decision.nombre_jours_accordes,
                    "nombre_jours_consommes":
                        decision.nombre_jours_consommes,
                    "reliquat_decision":
                        decision.reliquat,
                    "est_soldee":
                        decision.est_soldee,
                    "compteur": (
                        {
                            "id": compteur.id,
                            "jours_credites":
                                compteur.jours_credites,
                            "jours_debites":
                                compteur.jours_debites,
                            "reliquat":
                                compteur.reliquat,
                            "est_solde":
                                compteur.est_solde,
                        }
                        if compteur
                        else None
                    ),
                    "conges": conges,
                    "mouvements": mouvements,
                }
            )

        return Response(
            {
                "agent_id": agent_id,
                "decisions": resultats,
            }
        )