"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/serializers/permission.py

Description :
    Serializers des permissions.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth.models import Permission

from rest_framework import serializers


class PermissionSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des permissions.
    """

    class Meta:
        model = Permission

        fields = (
            "id",
            "name",
            "codename",
            "content_type",
        )


class PermissionReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des permissions.
    """

    application = serializers.CharField(
        source="content_type.app_label",
        read_only=True,
    )

    modele = serializers.CharField(
        source="content_type.model",
        read_only=True,
    )

    action = serializers.SerializerMethodField()

    def get_action(
        self,
        obj,
    ):
        """
        Retourne l'action de la permission.
        """

        return obj.codename.split(
            "_",
            1,
        )[0]

    class Meta:
        model = Permission

        fields = (
            "id",
            "name",
            "codename",
            "application",
            "modele",
            "action",
        )