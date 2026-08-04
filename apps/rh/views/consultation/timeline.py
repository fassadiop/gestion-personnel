from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.rh.models import Agent
from apps.rh.serializers.consultation.timeline import (
    TimelineSerializer,
)
from apps.rh.services.consultation import ConsultationService


class TimelineView(APIView):
    """
    Timeline de carrière d'un agent.
    """

    def get(self, request, agent_id):
        agent = get_object_or_404(
            Agent,
            pk=agent_id,
        )

        data = ConsultationService.timeline(
            agent=agent,
        )

        serializer = TimelineSerializer(
            data,
            many=True,
        )

        return Response(
            serializer.data
        )