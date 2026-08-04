from .consultation import ConsultationService
from .registry import ConsultationRegistry
from .providers import (
    DashboardProvider,
    CVCarriereProvider,
    TimelineProvider,
    StatistiquesProvider,
    OrganisationProvider,
)
from .constants import ConsultationProvider


ConsultationRegistry.register(
    ConsultationProvider.DASHBOARD,
    DashboardProvider,
)

ConsultationRegistry.register(
    ConsultationProvider.CV_CARRIERE,
    CVCarriereProvider,
)

ConsultationRegistry.register(
    ConsultationProvider.TIMELINE,
    TimelineProvider,
)

ConsultationRegistry.register(
    ConsultationProvider.STATISTIQUES,
    StatistiquesProvider,
)

ConsultationRegistry.register(
    ConsultationProvider.ORGANISATION,
    OrganisationProvider,
)


__all__ = [
    "ConsultationService",
]