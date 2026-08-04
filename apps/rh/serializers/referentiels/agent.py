from rest_framework import serializers

from apps.rh.models import Sexe

from apps.rh.models import Nationalite

from apps.rh.models import StatutAgent


class SexeSerializer(serializers.ModelSerializer):
    """
    Serializer de création/modification des sexes.
    """

    class Meta:
        model = Sexe

        fields = "__all__"


class SexeReadSerializer(serializers.ModelSerializer):
    """
    Serializer de consultation des sexes.
    """

    class Meta:
        model = Sexe

        fields = "__all__"


from rest_framework import serializers

from apps.rh.models import EtatCivil


class EtatCivilSerializer(serializers.ModelSerializer):
    """
    Serializer de création/modification des états civils.
    """

    class Meta:
        model = EtatCivil

        fields = "__all__"


class EtatCivilReadSerializer(serializers.ModelSerializer):
    """
    Serializer de consultation des états civils.
    """

    class Meta:
        model = EtatCivil

        fields = "__all__"


class NationaliteSerializer(serializers.ModelSerializer):
    """
    Serializer de création/modification des nationalités.
    """

    class Meta:
        model = Nationalite

        fields = "__all__"


class NationaliteReadSerializer(serializers.ModelSerializer):
    """
    Serializer de consultation des nationalités.
    """

    class Meta:
        model = Nationalite

        fields = "__all__"


class StatutAgentSerializer(serializers.ModelSerializer):
    """
    Serializer de création/modification des statuts d'agent.
    """

    class Meta:
        model = StatutAgent

        fields = "__all__"


class StatutAgentReadSerializer(serializers.ModelSerializer):
    """
    Serializer de consultation des statuts d'agent.
    """

    class Meta:
        model = StatutAgent

        fields = "__all__"