"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/reprise_service/reprise_service.py

Description :
    Serializers de la reprise de service.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import serializers

from apps.rh.models.reprise_service import (
    RepriseService,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)


class RepriseServiceSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la création
    et la modification d'une reprise de service.
    """

    class Meta:
        model = RepriseService

        fields = (
            "id",

            "date_reprise",

            "observation",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class RepriseServiceReadSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la consultation
    des reprises de service.
    """

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True,
        )
    )

    agent = AgentReadSerializer(
        source="evenement.agent",
        read_only=True,
    )

    class Meta:
        model = RepriseService

        fields = (
            "id",

            "evenement",

            "agent",

            "date_reprise",

            "observation",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )