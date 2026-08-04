from rest_framework import serializers

from apps.rh.models import (
    EvenementCarriere,
    PriseServiceInitiale,
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


class PriseServiceInitialeSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des prises de
    service initiales.
    """

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(
            actif=True
        )
    )

    structure = serializers.PrimaryKeyRelatedField(
        queryset=Structure.objects.filter(
            actif=True
        )
    )

    unite = serializers.PrimaryKeyRelatedField(
        queryset=UniteOrganisationnelle.objects.filter(
            actif=True
        ),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = PriseServiceInitiale

        fields = (
            "id",

            "evenement",

            "structure",
            "unite",

            "date_prise_service",

            "actif",

            "created_at",
            "updated_at",
        )

    def validate(self, attrs):

        structure = attrs.get("structure")
        unite = attrs.get("unite")

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


class PriseServiceInitialeReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des prises de service initiales.
    """

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
        model = PriseServiceInitiale

        fields = (
            "id",

            "evenement",

            "structure",
            "unite",

            "date_prise_service",

            "actif",

            "created_at",
            "updated_at",
        )