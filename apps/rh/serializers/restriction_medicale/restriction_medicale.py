"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/restriction_medicale/restriction_medicale.py

Description :
    Serializers de la restriction médicale.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import serializers

from apps.rh.models.restriction_medicale import (
    RestrictionMedicale,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)


class RestrictionMedicaleSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la création
    et la modification des restrictions
    médicales.
    """

    class Meta:
        model = RestrictionMedicale

        fields = (
            "id",

            "date_effet",

            "date_fin",

            "restriction",

            "observation",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class RestrictionMedicaleReadSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la consultation
    des restrictions médicales.
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
        model = RestrictionMedicale

        fields = (
            "id",

            "evenement",

            "agent",

            "date_effet",

            "date_fin",

            "restriction",

            "observation",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )