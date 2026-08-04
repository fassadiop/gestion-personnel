# apps/rh/serializers/conge_maladie/conge_maladie.py

from rest_framework import serializers

from apps.rh.models.conge_maladie import CongeMaladie


class CongeMaladieSerializer(serializers.ModelSerializer):
    """
    Serializer d'écriture du congé de maladie.
    """

    class Meta:
        model = CongeMaladie

        fields = (
            "id",
            "evenement",
            "debut_conge",
            "fin_conge",
        )


class CongeMaladieReadSerializer(serializers.ModelSerializer):
    """
    Serializer de lecture du congé de maladie.
    """

    nombre_jours = serializers.ReadOnlyField()

    class Meta:
        model = CongeMaladie

        fields = (
            "id",
            "evenement",
            "debut_conge",
            "fin_conge",
            "nombre_jours",
            "created_at",
            "updated_at",
        )