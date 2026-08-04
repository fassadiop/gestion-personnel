"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/conges/mouvement_compteur_conge.py

Description :
    Serializers des mouvements de compteur
    de congé.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.serializers.agent.agent import AgentReadSerializer
from apps.rh.serializers.conges.decision_conge import DecisionCongeReadSerializer
from rest_framework import serializers

from apps.rh.models import (
    TypeMouvementConge,
)

from apps.rh.models.compteur_conge import CompteurConge
from apps.rh.models.mouvement_compteur_conge import MouvementCompteurConge
from apps.rh.serializers.conges.compteur_conge import (
    CompteurCongeReadSerializer,
)

from apps.rh.serializers.referentiels.rh.type_mouvement_conge import (
    TypeMouvementCongeReadSerializer,
)


class MouvementCompteurCongeSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des mouvements
    de compteur de congé.
    """

    compteur = serializers.PrimaryKeyRelatedField(
        queryset=CompteurConge.objects.filter(
            actif=True
        )
    )

    type_mouvement = serializers.PrimaryKeyRelatedField(
        queryset=TypeMouvementConge.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = MouvementCompteurConge

        fields = (
            "id",

            "compteur",

            "type_mouvement",

            "nombre_jours",

            "date_mouvement",

            "observation",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class MouvementCompteurCongeReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des mouvements de compteur de congé.
    """

    compteur = (
        CompteurCongeReadSerializer(
            read_only=True
        )
    )

    type_mouvement = (
        TypeMouvementCongeReadSerializer(
            read_only=True
        )
    )

    agent = AgentReadSerializer(
        source="compteur.agent",
        read_only=True,
    )

    decision_conge = DecisionCongeReadSerializer(
        source="compteur.decision_conge",
        read_only=True,
    )

    sens = serializers.ReadOnlyField()

    impact = serializers.ReadOnlyField()

    class Meta:
        model = MouvementCompteurConge

        fields = (
            "id",

            "compteur",

            "decision_conge",

            "agent",

            "type_mouvement",

            "nombre_jours",

            "sens",

            "impact",

            "date_mouvement",

            "observation",

            "created_at",

            "updated_at",
        )