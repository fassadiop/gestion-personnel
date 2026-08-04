"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/serializers/groupe.py

Description :
    Serializers des groupes (rôles).

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth.models import Group

from rest_framework import serializers

from apps.administration.serializers.permission import (
    PermissionReadSerializer,
)


class GroupeSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création
    et la modification des groupes.
    """

    class Meta:
        model = Group

        fields = (
            "id",
            "name",
            "permissions",
        )


class GroupeReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des groupes.
    """

    nombre_utilisateurs = serializers.SerializerMethodField()

    class Meta:
        model = Group

        fields = (
            "id",
            "name",
            "nombre_utilisateurs",
        )

    def get_nombre_utilisateurs(
        self,
        obj,
    ):
        """
        Retourne le nombre d'utilisateurs
        appartenant au groupe.
        """

        return obj.user_set.count()


class GroupeSimpleSerializer(serializers.ModelSerializer):
    """
    Serializer léger utilisé
    dans les autres serializers.
    """

    class Meta:
        model = Group

        fields = (
            "id",
            "name",
        )


class GroupeDetailSerializer(
    serializers.ModelSerializer,
):
    """
    Consultation détaillée d'un groupe.
    """

    nombre_utilisateurs = serializers.SerializerMethodField()

    permissions = PermissionReadSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = Group

        fields = (
            "id",
            "name",
            "nombre_utilisateurs",
            "permissions",
        )

    def get_nombre_utilisateurs(
        self,
        obj,
    ):
        return obj.user_set.count()