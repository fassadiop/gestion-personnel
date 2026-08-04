from apps.rh.services.consultation.base import (
    BaseConsultationProvider,
)
from apps.rh.services.consultation.constants import (
    ConsultationProvider,
)
from apps.rh.services.consultation.statistiques import (
    StatistiquesService,
)


class StatistiquesProvider(BaseConsultationProvider):
    """
    Provider des statistiques RH agrégées.
    """

    provider = ConsultationProvider.STATISTIQUES

    @classmethod
    def process(cls, **kwargs):
        return StatistiquesService.execute()