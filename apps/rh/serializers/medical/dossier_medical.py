from rest_framework import serializers

from apps.rh.models import (
    Agent,
    DossierMedical,
)


from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)


class DossierMedicalSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des dossiers médicaux.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    class Meta:
        model = DossierMedical

        fields = (
            "id",

            "agent",

            "groupe_sanguin",
            "allergies",
            "antecedents_medicaux",
            "traitements_en_cours",
            "medecin_traitant",
            "telephone_medecin",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )


class DossierMedicalReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des dossiers médicaux.
    """

    agent = AgentReadSerializer(
        read_only=True
    )

    class Meta:
        model = DossierMedical

        fields = (
            "id",

            "agent",

            "groupe_sanguin",
            "allergies",
            "antecedents_medicaux",
            "traitements_en_cours",
            "medecin_traitant",
            "telephone_medecin",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )