"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : authentication/serializers.py

Description :
    Serializers utilisés pour
    l'authentification.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth import authenticate, get_user_model

from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    """
    Serializer de connexion.
    """

    username = serializers.CharField()

    password = serializers.CharField(
        write_only=True,
        style={
            "input_type": "password",
        },
    )

    def validate(
        self,
        attrs,
    ):
        """
        Vérifie les identifiants
        de connexion.
        """

        user = authenticate(
            username=attrs["username"],
            password=attrs["password"],
        )

        if user is None:
            raise serializers.ValidationError(
                "Identifiants invalides."
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "Ce compte est désactivé."
            )

        attrs["user"] = user

        return attrs


class RefreshTokenSerializer(
    serializers.Serializer
):
    """
    Serializer de rafraîchissement
    du token JWT.
    """

    refresh = serializers.CharField()


class CurrentUserSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer de l'utilisateur connecté.
    """

    groupes = serializers.SerializerMethodField()

    permissions = serializers.SerializerMethodField()

    class Meta:

        model = User

        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_superuser",
            "groupes",
            "permissions",
        )

    def get_groupes(
        self,
        obj,
    ):
        return list(
            obj.groups.values_list(
                "name",
                flat=True,
            )
        )

    def get_permissions(
        self,
        obj,
    ):
        return sorted(
            obj.get_all_permissions(),
        )