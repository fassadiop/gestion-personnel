from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from apps.rh.models import Agent
from apps.rh.serializers.consultation.cv_carriere.cv_carriere import (
    CVCarriereSerializer,
)
from apps.rh.services.consultation import ConsultationService


class CVCarriereView(APIView):
    """
    Consultation du CV de carrière consolidé
    d'un agent.
    """

    def get(self, request, agent_id):
        agent = get_object_or_404(
            Agent,
            pk=agent_id,
        )

        data = ConsultationService.cv_carriere(
            agent=agent,
        )

        serializer = CVCarriereSerializer(
            data,
            context={"request": request},
        )

        return Response(
            serializer.data
        )