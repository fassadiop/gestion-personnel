"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/serializers/utilisateur_update.py

Description :
    Serializer de modification d'un compte utilisateur.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import serializers

User = get_user_model()


class UtilisateurUpdateSerializer(
    serializers.Serializer
):
    """
    Contrat de modification
    d'un compte utilisateur.
    """

    email = serializers.EmailField(
        required=False,
        allow_blank=True,
    )

    is_active = serializers.BooleanField(
        required=False,
    )

    groupes = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        many=True,
        required=False,
    )

    def validate_email(
        self,
        value,
    ):
        """
        Vérifie que l'adresse e-mail
        n'est pas déjà utilisée.
        """

        user = self.context.get("user")

        queryset = User.objects.filter(
            email=value,
        )

        if user:
            queryset = queryset.exclude(
                pk=user.pk,
            )

        if value and queryset.exists():
            raise serializers.ValidationError(
                "Cette adresse e-mail est déjà utilisée."
            )

        return value