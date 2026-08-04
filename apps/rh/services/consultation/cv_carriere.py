from apps.rh.models import EvenementCarriere


class CVCarriereService:
    """
    Service de consultation du CV de carrière d'un agent.

    Agrège les informations administratives courantes
    et l'historique de carrière de l'agent.
    """

    @classmethod
    def execute(cls, agent):
        return {
            "agent": agent,
            "situation_administrative": (
                agent.situation_administrative_courante
            ),
            "affectation": agent.affectation_courante,
            "occupation": agent.occupation_courante,
            "evenements": cls.get_evenements(agent),
        }

    @staticmethod
    def get_evenements(agent):
        """
        Retourne l'historique des événements
        de carrière de l'agent.
        """

        return (
            EvenementCarriere.objects
            .filter(agent=agent)
            .select_related(
                "type_evenement",
                "statut",
                "position_administrative",
            )
            .order_by(
                "-date_effet",
                "-id",
            )
        )