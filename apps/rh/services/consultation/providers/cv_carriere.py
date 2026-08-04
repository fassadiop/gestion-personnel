from apps.rh.services.consultation.base import (
    BaseConsultationProvider,
)
from apps.rh.services.consultation.constants import (
    ConsultationProvider,
)
from apps.rh.services.consultation.cv_carriere import (
    CVCarriereService,
)


class CVCarriereProvider(BaseConsultationProvider):
    """
    Provider du CV de carrière d'un agent.
    """

    provider = ConsultationProvider.CV_CARRIERE

    @classmethod
    def process(cls, agent, **kwargs):
        return CVCarriereService.execute(
            agent=agent,
        )