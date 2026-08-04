from apps.rh.services.consultation.base import BaseConsultationProvider
from apps.rh.services.consultation.constants import ConsultationProvider

from apps.rh.services.consultation.dashboard.kpi import DashboardKPIService
from apps.rh.services.consultation.dashboard.statistiques import (
    DashboardStatistiquesService,
)
from apps.rh.services.consultation.dashboard.evenements import (
    DashboardEvenementService,
)
from apps.rh.services.consultation.dashboard.alertes import (
    DashboardAlerteService,
)


class DashboardProvider(BaseConsultationProvider):
    """
    Provider du tableau de bord.
    """

    provider = ConsultationProvider.DASHBOARD

    @classmethod
    def process(cls, **kwargs):
        return {
            "kpi": DashboardKPIService.execute(),
            "statistiques": DashboardStatistiquesService.execute(),
            "derniers_evenements": DashboardEvenementService.execute(),
            "alertes": DashboardAlerteService.execute(),
        }