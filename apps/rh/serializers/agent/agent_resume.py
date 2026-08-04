"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier :
    apps/rh/serializers/agent_resume.py

Description :
    Serializer résumé d'un agent.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import serializers

from apps.rh.models import Agent


class AgentResumeSerializer(
    serializers.ModelSerializer
):
    """
    Résumé d'un agent.

    Utilisé par les modules externes
    (Administration, Documents, Santé...)
    lorsqu'il n'est pas nécessaire
    d'exposer tout le dossier RH.
    """

    class Meta:
        model = Agent

        fields = (
            "id",

            "matricule",

            "nom",

            "prenom",

            "structure_racine",

            "actif",
        )