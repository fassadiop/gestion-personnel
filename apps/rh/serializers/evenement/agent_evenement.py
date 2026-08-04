"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/evenement/agent_evenement.py

Description :
    Serializer de l'agent utilisé dans
    la consultation des événements de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import serializers

from apps.rh.models import Agent


class AgentEvenementReadSerializer(
    serializers.ModelSerializer
):
    """
    Informations de l'agent nécessaires
    à la consultation d'un événement.
    """

    corps = serializers.SerializerMethodField()

    grade = serializers.SerializerMethodField()

    classe = serializers.SerializerMethodField()

    echelon = serializers.SerializerMethodField()

    structure = serializers.SerializerMethodField()

    poste = serializers.SerializerMethodField()

    class Meta:
        model = Agent

        fields = (
            "id",

            "matricule",
            "nom",
            "prenom",

            "corps",
            "grade",
            "classe",
            "echelon",

            "structure",
            "poste",
        )

    def get_corps(self, obj):
        situation = obj.situation_administrative_courante

        if not situation or not situation.corps:
            return None

        return situation.corps.libelle

    def get_grade(self, obj):
        situation = obj.situation_administrative_courante

        if not situation or not situation.grade:
            return None

        return situation.grade.libelle

    def get_classe(self, obj):
        situation = obj.situation_administrative_courante

        if not situation or not situation.classe:
            return None

        return situation.classe.libelle

    def get_echelon(self, obj):
        situation = obj.situation_administrative_courante

        if not situation or not situation.echelon:
            return None

        return situation.echelon.libelle

    def get_structure(self, obj):
        affectation = obj.affectation_courante

        if (
            not affectation
            or not affectation.structure
        ):
            return None

        return affectation.structure.nom

    def get_poste(self, obj):
        occupation = obj.occupation_courante

        if (
            not occupation
            or not occupation.poste
        ):
            return None

        return occupation.poste.nom