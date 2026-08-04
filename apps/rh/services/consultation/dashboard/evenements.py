from apps.rh.models import EvenementCarriere


class DashboardEvenementService:
    """
    Service de récupération des derniers événements de carrière.
    """

    DEFAULT_LIMIT = 10

    @classmethod
    def execute(cls, limit=None):
        if limit is None:
            limit = cls.DEFAULT_LIMIT

        return (
            EvenementCarriere.objects
            .select_related(
                "agent",
                "type_evenement",
                "statut",
            )
            .order_by("-created_at", "-id")[:limit]
        )