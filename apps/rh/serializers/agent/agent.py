from rest_framework import serializers

from apps.rh.models import (
    Agent,
)


class AgentSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des agents.
    """

    class Meta:
        model = Agent

        fields = (
            "id",

            "matricule",
            "nom",
            "prenom",
            "sexe",
            "date_naissance",
            "lieu_naissance",
            "nationalite",
            "etat_civil",
            "telephone",
            "email",
            "adresse",

            "statut",
            "numero_solde",
            "nom_jeune_fille",

            "date_recrutement",

            "photo",

            "actif",

            "created_at",
            "updated_at",
        )


class AgentReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des agents.
    """

    class Meta:
        model = Agent

        fields = (
            "id",

            "matricule",
            "nom",
            "prenom",
            "sexe",
            "date_naissance",
            "lieu_naissance",
            "nationalite",
            "statut",
            "telephone",
            "email",
            "adresse",
            "etat_civil",
            "date_recrutement",
            "numero_solde",
            "photo",
            "nom_jeune_fille",
            "actif",

            "created_at",
            "updated_at",
        )