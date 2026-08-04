from rest_framework import serializers


class RepartitionSerializer(serializers.Serializer):
    """
    Élément générique d'une répartition statistique.
    """

    code = serializers.CharField(
        allow_null=True,
        required=False,
    )

    libelle = serializers.CharField(
        allow_null=True,
        required=False,
    )

    nombre = serializers.IntegerField()