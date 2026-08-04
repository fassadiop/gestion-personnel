from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.rh.serializers.consultation.dashboard.dashboard import DashboardSerializer
from apps.rh.services.consultation import ConsultationService


class DashboardView(APIView):
    """
    Tableau de bord RH.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = ConsultationService.dashboard()

        serializer = DashboardSerializer(instance=data)

        return Response(serializer.data)