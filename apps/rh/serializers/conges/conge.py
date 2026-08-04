"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/conges/conge.py

Description :
    Serializers des congés.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.serializers.agent.agent import AgentReadSerializer
from rest_framework import serializers

from apps.rh.models import (
    Conge,
    DecisionConge,
)

from apps.rh.serializers.conges.decision_conge import (
    DecisionCongeReadSerializer,
)


class CongeSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des congés.
    """

    decision_conge = serializers.PrimaryKeyRelatedField(
        queryset=DecisionConge.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = Conge

        fields = (
            "id",

            "decision_conge",

            "date_cessation_service",

            "date_reprise",

            "observation",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class CongeReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des congés.
    """

    decision_conge = (
        DecisionCongeReadSerializer(
            read_only=True
        )
    )

    agent = AgentReadSerializer(
        source="decision_conge.agent",
        read_only=True,
    )

    nombre_jours = serializers.ReadOnlyField()

    numero_tranche = serializers.ReadOnlyField()

    est_fractionnement = serializers.ReadOnlyField()

    class Meta:
        model = Conge

        fields = (
            "id",

            "decision_conge",

            "agent",

            "date_cessation_service",

            "date_reprise",

            "nombre_jours",

            "numero_tranche",

            "est_fractionnement",

            "observation",

            "created_at",

            "updated_at",
        )