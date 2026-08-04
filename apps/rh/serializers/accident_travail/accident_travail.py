"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/accident_travail/accident_travail.py

Description :
    Serializers de l'accident de travail.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import serializers

from apps.rh.models.accident_travail import (
    AccidentTravail,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)


class AccidentTravailSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la création
    et la modification d'un accident de travail.
    """

    class Meta:
        model = AccidentTravail

        fields = (
            "id",

            "date_accident",

            "lieu_accident",

            "circonstances",

            "consequences",

            "observation",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class AccidentTravailReadSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la consultation
    des accidents de travail.
    """

    evenement = EvenementCarriereReadSerializer(
        read_only=True,
    )

    agent = AgentReadSerializer(
        source="evenement.agent",
        read_only=True,
    )

    class Meta:
        model = AccidentTravail

        fields = (
            "id",

            "evenement",

            "agent",

            "date_accident",

            "lieu_accident",

            "circonstances",

            "consequences",

            "observation",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )