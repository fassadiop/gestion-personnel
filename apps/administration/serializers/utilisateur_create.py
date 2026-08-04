"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/administration/serializers/utilisateur_create.py

Description :
    Serializer de création d'un compte utilisateur.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.contrib.auth.models import Group

from rest_framework import serializers

from apps.rh.models.agent import Agent


class UtilisateurCreateSerializer(
    serializers.Serializer
):
    """
    Contrat de création
    d'un compte utilisateur.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(
            actif=True,
            user__isnull=True,
        )
    )

    groupes = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        many=True,
        required=False,
    )