from rest_framework.response import Response
from rest_framework.views import APIView

from apps.rh.serializers.consultation.statistiques.statistiques import (
    StatistiquesSerializer,
)
from apps.rh.services.consultation import ConsultationService


class StatistiquesView(APIView):
    """
    Statistiques RH agrégées.
    """

    def get(self, request):
        data = ConsultationService.statistiques()

        serializer = StatistiquesSerializer(
            data
        )

        return Response(
            serializer.data
        )