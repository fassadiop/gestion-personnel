from rest_framework import serializers

from apps.rh.models import EvenementCarriere


class TimelineSerializer(serializers.ModelSerializer):
    """
    Serializer d'un événement de la timeline
    de carrière d'un agent.
    """

    type_evenement = serializers.StringRelatedField()
    statut = serializers.StringRelatedField()
    position_administrative = serializers.StringRelatedField()

    class Meta:
        model = EvenementCarriere

        fields = (
            "id",
            "type_evenement",
            "statut",
            "position_administrative",
            "date_effet",
            "date_fin",
            "reference_acte",
            "objet",
            "description",
            "observation",
        )