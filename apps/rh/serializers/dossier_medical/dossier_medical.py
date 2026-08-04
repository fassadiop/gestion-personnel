# apps/rh/serializers/dossier_medical/dossier_medical.py

from rest_framework import serializers

from apps.rh.serializers.agent.agent import AgentReadSerializer
from apps.rh.serializers.documents.documents import DocumentReadSerializer
from apps.rh.serializers.evenement.evenement import EvenementCarriereReadSerializer


class EtatMedicalSerializer(serializers.Serializer):
    """
    État médical courant de l'agent.
    """

    statut = serializers.CharField()

    evenement = EvenementCarriereReadSerializer(
        allow_null=True
    )


class ResumeMedicalSerializer(serializers.Serializer):
    """
    Résumé du dossier médical.
    """

    nombre_evenements = serializers.IntegerField()
    nombre_documents = serializers.IntegerField()

    dernier_conge_maladie = EvenementCarriereReadSerializer(
        allow_null=True
    )

    derniere_restriction = EvenementCarriereReadSerializer(
        allow_null=True
    )

    derniere_inaptitude = EvenementCarriereReadSerializer(
        allow_null=True
    )

    dernier_accident = EvenementCarriereReadSerializer(
        allow_null=True
    )

    etat_medical = EtatMedicalSerializer()


class HistoriqueMedicalSerializer(serializers.Serializer):
    """
    Un événement médical accompagné
    de ses documents justificatifs.
    """

    evenement = EvenementCarriereReadSerializer()

    documents = DocumentReadSerializer(
        many=True
    )


class DossierMedicalSerializer(serializers.Serializer):
    """
    Dossier médical complet.
    """

    agent = AgentReadSerializer()

    resume = ResumeMedicalSerializer()

    historique = HistoriqueMedicalSerializer(
        many=True
    )