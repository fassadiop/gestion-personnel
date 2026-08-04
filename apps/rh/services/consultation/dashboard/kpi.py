from django.utils import timezone

from apps.rh.models import (
    Agent,
    Conge,
    DocumentAgent,
    EvenementCarriere,
)


class DashboardKPIService:
    """
    Service de calcul des indicateurs du tableau de bord.
    """

    @classmethod
    def execute(cls):
        return {
            "agents": cls.total_agents(),
            "documents": cls.total_documents(),
            "evenements": cls.total_evenements(),
            "conges": cls.total_conges(),
        }

    @classmethod
    def total_agents(cls):
        return Agent.objects.count()

    @classmethod
    def total_documents(cls):
        return DocumentAgent.objects.count()

    @classmethod
    def total_evenements(cls):
        return EvenementCarriere.objects.count()


    @classmethod
    def total_conges(cls):
        aujourd_hui = timezone.localdate()

        return Conge.objects.filter(
            date_cessation_service__lte=aujourd_hui,
            date_reprise__gt=aujourd_hui,
        ).count()