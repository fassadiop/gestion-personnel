from typing import Any

from .constants import ConsultationProvider
from .registry import ConsultationRegistry


class ConsultationService:
    """
    Façade du moteur de consultation.
    """

    @classmethod
    def execute(cls, provider: str, **kwargs) -> Any:
        provider_class = ConsultationRegistry.get(provider)
        return provider_class.execute(**kwargs)

    @classmethod
    def dashboard(cls):
        return cls.execute(
            ConsultationProvider.DASHBOARD
        )

    @classmethod
    def cv_carriere(cls, agent, **kwargs):
        return cls.execute(
            ConsultationProvider.CV_CARRIERE,
            agent=agent,
            **kwargs,
        )

    @classmethod
    def timeline(cls, agent, **kwargs):
        return cls.execute(
            ConsultationProvider.TIMELINE,
            agent=agent,
            **kwargs,
        )

    @classmethod
    def organisation(cls, **kwargs):
        return cls.execute(
            ConsultationProvider.ORGANISATION,
            **kwargs,
        )

    @classmethod
    def statistiques(cls, **kwargs):
        return cls.execute(
            ConsultationProvider.STATISTIQUES,
            **kwargs,
        )