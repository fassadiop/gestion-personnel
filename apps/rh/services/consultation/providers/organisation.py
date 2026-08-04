from apps.rh.services.consultation.base import (
    BaseConsultationProvider,
)
from apps.rh.services.consultation.constants import (
    ConsultationProvider,
)
from apps.rh.services.consultation.organisation_tree import (
    OrganisationTreeService,
)


class OrganisationProvider(BaseConsultationProvider):
    """
    Provider de l'arborescence organisationnelle.
    """

    provider = ConsultationProvider.ORGANISATION

    @classmethod
    def process(cls, **kwargs):
        return OrganisationTreeService.execute()