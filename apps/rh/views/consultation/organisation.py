from rest_framework.response import Response
from rest_framework.views import APIView

from apps.rh.serializers.consultation.organisation import (
    OrganisationTreeSerializer,
)
from apps.rh.services.consultation import ConsultationService


class OrganisationTreeView(APIView):
    """
    Arborescence organisationnelle complète.
    """

    def get(self, request):
        data = ConsultationService.organisation()

        serializer = OrganisationTreeSerializer(
            data
        )

        return Response(
            serializer.data
        )