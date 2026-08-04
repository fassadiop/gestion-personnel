from apps.rh.models import EvenementCarriere


class TimelineService:
    """
    Service de consultation de la timeline
    de carrière d'un agent.

    Retourne chronologiquement les événements
    constituant le parcours de carrière de l'agent.
    """

    @classmethod
    def execute(cls, agent):
        return (
            EvenementCarriere.objects
            .filter(agent=agent)
            .select_related(
                "type_evenement",
                "statut",
                "position_administrative",
            )
            .order_by(
                "date_effet",
                "id",
            )
        )