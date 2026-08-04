from rest_framework import serializers

from apps.rh.models import Nomination
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Structure,
    UniteOrganisationnelle,
    Poste,
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

from apps.rh.serializers.organisation.poste import (
    PosteReadSerializer,
)


class NominationSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des nominations.
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
        required=False,
        allow_null=True,
    )

    poste = serializers.PrimaryKeyRelatedField(
        queryset=Poste.objects.filter(
            actif=True
        )
    )

    class Meta:
        model = Nomination

        fields = (
            "id",

            "evenement",

            "structure",
            "unite",
            "poste",

            "created_at",
            "updated_at",
        )


class NominationReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des nominations.
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

    poste = PosteReadSerializer(
        read_only=True
    )

    class Meta:
        model = Nomination

        fields = (
            "id",

            "evenement",

            "structure",
            "unite",
            "poste",

            "created_at",
            "updated_at",
        )