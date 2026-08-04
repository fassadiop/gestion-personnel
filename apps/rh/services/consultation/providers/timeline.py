from apps.rh.services.consultation.base import (
    BaseConsultationProvider,
)
from apps.rh.services.consultation.constants import (
    ConsultationProvider,
)
from apps.rh.services.consultation.timeline import (
    TimelineService,
)


class TimelineProvider(BaseConsultationProvider):
    """
    Provider de la timeline de carrière d'un agent.
    """

    provider = ConsultationProvider.TIMELINE

    @classmethod
    def process(cls, agent, **kwargs):
        return TimelineService.execute(
            agent=agent,
        )