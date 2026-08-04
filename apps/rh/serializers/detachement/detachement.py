
from rest_framework import serializers

from apps.rh.models import (
    Detachement,
    EvenementCarriere,
    Structure,
    UniteOrganisationnelle,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)

from apps.rh.serializers.organisation.structure import (
    StructureReadSerializer,
)

from apps.rh.serializers.organisation.unite_organisationnelle import (
    UniteOrganisationnelleReadSerializer,
)


class DetachementSerializer(
    serializers.ModelSerializer
):

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(
            actif=True
        )
    )

    structure = serializers.PrimaryKeyRelatedField(
        queryset=Structure.objects.filter(
            actif=True
        ),
        allow_null=True,
        required=False,
    )

    unite = serializers.PrimaryKeyRelatedField(
        queryset=UniteOrganisationnelle.objects.filter(
            actif=True
        ),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Detachement

        fields = (
            "id",
            "evenement",
            "organisme_accueil",
            "structure",
            "unite",
            "date_debut",
            "date_fin",
            "created_at",
            "updated_at",
        )

    def validate(self, attrs):

        structure = attrs.get("structure")
        unite = attrs.get("unite")

        if unite and structure is None:
            raise serializers.ValidationError(
                {
                    "structure": (
                        "La structure est obligatoire "
                        "lorsqu'une unité est renseignée."
                    )
                }
            )

        if (
            unite
            and
            unite.structure != structure
        ):
            raise serializers.ValidationError(
                {
                    "unite": (
                        "L'unité organisationnelle "
                        "n'appartient pas à la "
                        "structure sélectionnée."
                    )
                }
            )

        return attrs


class DetachementReadSerializer(
    serializers.ModelSerializer
):

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True
        )
    )

    structure = StructureReadSerializer(
        read_only=True
    )

    unite = (
        UniteOrganisationnelleReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = Detachement

        fields = (
            "id",
            "evenement",
            "organisme_accueil",
            "structure",
            "unite",
            "date_debut",
            "date_fin",
            "created_at",
            "updated_at",
        )