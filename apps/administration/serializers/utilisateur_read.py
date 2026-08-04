"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/serializers/utilisateur_read.py

Description :
    Serializer de consultation des utilisateurs.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.rh.serializers.agent import (
    AgentReadSerializer,
)

from apps.rh.serializers.organisation.structure import (
    StructureReadSerializer,
)

User = get_user_model()


class UtilisateurReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des utilisateurs.
    """

    agent = AgentReadSerializer(
        read_only=True,
    )

    structure_racine = serializers.SerializerMethodField()

    roles = serializers.SerializerMethodField()

    class Meta:
        model = User

        fields = (
            "id",

            "username",

            "email",

            "agent",

            "structure_racine",

            "roles",

            "is_active",

            "is_superuser",

            "last_login",

            "date_joined",
        )

    def get_structure_racine(
        self,
        obj,
    ):

        if (
            not hasattr(obj, "agent")
            or obj.agent is None
        ):
            return None

        return StructureReadSerializer(
            obj.agent.structure_racine
        ).data

    def get_roles(
        self,
        obj,
    ):

        return [
            {
                "id": role.id,
                "nom": role.name,
            }
            for role in obj.groups.all()
        ]