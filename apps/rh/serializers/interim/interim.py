from rest_framework import serializers

from apps.rh.models import (
    EvenementCarriere,
    Interim,
    Poste,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)

from apps.rh.serializers.organisation.poste import (
    PosteReadSerializer,
)


class InterimSerializer(serializers.ModelSerializer):

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(
            actif=True
        )
    )

    poste = serializers.PrimaryKeyRelatedField(
        queryset=Poste.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = Interim

        fields = (
            "id",
            "evenement",
            "poste",
            "created_at",
            "updated_at",
        )


class InterimReadSerializer(serializers.ModelSerializer):

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    poste = PosteReadSerializer(
        read_only=True
    )

    class Meta:
        model = Interim

        fields = (
            "id",
            "evenement",
            "poste",
            "created_at",
            "updated_at",
        )