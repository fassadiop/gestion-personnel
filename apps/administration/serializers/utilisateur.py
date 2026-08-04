# apps/administration/serializers/utilisateur.py

from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.administration.serializers.profil_administration import (
    ProfilAdministrationReadSerializer,
)

from apps.administration.serializers.groupe import (
    GroupeSimpleSerializer,
)

User = get_user_model()


class UtilisateurSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création
    et la modification d'un utilisateur.
    """

    class Meta:
        model = User

        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
        )


class UtilisateurReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des utilisateurs du SGCP.
    """

    profil_administration = (
        ProfilAdministrationReadSerializer(
            read_only=True
        )
    )

    groupes = GroupeSimpleSerializer(
        many=True,
        source="groups",
        read_only=True,
    )

    class Meta:
        model = User

        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_superuser",
            "profil_administration",
            "groupes",
            "last_login",
            "date_joined",
        )