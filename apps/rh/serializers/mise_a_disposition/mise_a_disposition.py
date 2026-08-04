from rest_framework import serializers

from apps.rh.models import (
    EvenementCarriere,
    Structure,
    UniteOrganisationnelle,
)

from apps.rh.models.mise_a_disposition import MiseADisposition

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)

from apps.rh.serializers.organisation.structure import (
    StructureReadSerializer,
)

from apps.rh.serializers.organisation.unite_organisationnelle import (
    UniteOrganisationnelleReadSerializer,
)


class MiseADispositionSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des mises à disposition.
    """

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
        model = MiseADisposition

        fields = (
            "id",

            "evenement",

            "organisme_accueil",

            "structure",
            "unite",

            "date_debut",
            "date_fin",

            "actif",

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


class MiseADispositionReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des mises à disposition.
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
        model = MiseADisposition

        fields = (
            "id",

            "evenement",

            "organisme_accueil",

            "structure",
            "unite",

            "date_debut",
            "date_fin",

            "actif",

            "created_at",
            "updated_at",
        )