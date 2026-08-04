# apps/rh/views/dossier_medical/dossier_medical.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.rh.serializers.dossier_medical.dossier_medical import DossierMedicalSerializer
from apps.rh.services.dossier_medical import DossierMedicalService


class DossierMedicalView(APIView):
    """
    Retourne le dossier médical complet d'un agent.
    """

    def get(self, request, agent_id):
        service = DossierMedicalService(agent_id)
        dossier = service.get_dossier()

        serializer = DossierMedicalSerializer(dossier)

        return Response(serializer.data, status=status.HTTP_200_OK)