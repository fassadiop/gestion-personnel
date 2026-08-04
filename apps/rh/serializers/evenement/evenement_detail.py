"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/evenement/evenement_detail.py

Description :
    Serializer de consultation détaillée
    d'un événement de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import serializers

from apps.rh.models.evenement import (
    EvenementCarriere,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)

from apps.rh.serializers.referentiels.evenement.statut_evenement import (
    StatutEvenementReadSerializer,
)

from apps.rh.serializers.referentiels.evenement.type_evenement import (
    TypeEvenementReadSerializer,
)

from apps.rh.serializers.referentiels.statut.position_administrative import (
    PositionAdministrativeReadSerializer,
)


class EvenementCarriereDetailSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    détaillée d'un événement de carrière.
    """

    agent = AgentReadSerializer(
        read_only=True
    )

    type_evenement = (
        TypeEvenementReadSerializer(
            read_only=True
        )
    )

    statut = (
        StatutEvenementReadSerializer(
            read_only=True
        )
    )

    position_administrative = (
        PositionAdministrativeReadSerializer(
            read_only=True
        )
    )

    documents = serializers.SerializerMethodField()

    historique = serializers.SerializerMethodField()

    class Meta:
        model = EvenementCarriere

        fields = (
            "id",

            "agent",

            "type_evenement",

            "statut",

            "position_administrative",

            "date_effet",
            "date_fin",

            "reference_acte",
            "objet",
            "description",
            "observation",

            "documents",
            "historique",

            "actif",

            "created_at",
            "updated_at",
        )

    def get_documents(
        self,
        obj,
    ):
        """
        Documents administratifs associés.

        Implémentation à venir.
        """

        return []

    def get_historique(
        self,
        obj,
    ):
        """
        Historique des traitements.

        Implémentation à venir.
        """

        return []