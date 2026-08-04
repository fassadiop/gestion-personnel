"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/conges/compteur_conge.py

Description :
    Serializers des compteurs de congé.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.serializers.agent.agent import AgentReadSerializer
from apps.rh.serializers.referentiels.rh.type_conge import TypeCongeReadSerializer
from rest_framework import serializers

from apps.rh.models import (
    DecisionConge,
)

from apps.rh.models.compteur_conge import CompteurConge
from apps.rh.serializers.conges.decision_conge import (
    DecisionCongeReadSerializer,
)


class CompteurCongeSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des compteurs
    de congé.
    """

    decision_conge = serializers.PrimaryKeyRelatedField(
        queryset=DecisionConge.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = CompteurConge

        fields = (
            "id",

            "decision_conge",

            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class CompteurCongeReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des compteurs de congé.
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

    type_conge = TypeCongeReadSerializer(
        source="decision_conge.type_conge",
        read_only=True,
    )

    jours_accordes = serializers.ReadOnlyField()

    jours_consommes = serializers.ReadOnlyField()

    reliquat = serializers.ReadOnlyField()

    est_solde = serializers.ReadOnlyField()

    class Meta:
        model = CompteurConge

        fields = (
            "id",

            "decision_conge",

            "agent",

            "type_conge",

            "jours_accordes",

            "jours_consommes",

            "reliquat",

            "est_solde",

            "created_at",

            "updated_at",
        )