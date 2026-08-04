from rest_framework import serializers

from apps.rh.models import Recrutement
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import (
    Structure,
    UniteOrganisationnelle,
    Poste,
)
from apps.rh.models.referentiels import (
    Corps,
    Grade,
    Classe,
    Echelon,
    PositionAdministrative,
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
from apps.rh.serializers.referentiels.statut.corps import (
    CorpsReadSerializer,
)
from apps.rh.serializers.referentiels.statut.grade import (
    GradeReadSerializer,
)
from apps.rh.serializers.referentiels.statut.classe import (
    ClasseReadSerializer,
)
from apps.rh.serializers.referentiels.statut.echelon import (
    EchelonReadSerializer,
)
from apps.rh.serializers.referentiels.statut.position_administrative import (
    PositionAdministrativeReadSerializer,
)


class RecrutementSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des recrutements.
    """

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(actif=True)
    )

    corps = serializers.PrimaryKeyRelatedField(
        queryset=Corps.objects.filter(actif=True)
    )

    grade = serializers.PrimaryKeyRelatedField(
        queryset=Grade.objects.filter(actif=True)
    )

    classe = serializers.PrimaryKeyRelatedField(
        queryset=Classe.objects.filter(actif=True)
    )

    echelon = serializers.PrimaryKeyRelatedField(
        queryset=Echelon.objects.filter(actif=True)
    )

    structure = serializers.PrimaryKeyRelatedField(
        queryset=Structure.objects.filter(actif=True)
    )

    class Meta:
        model = Recrutement

        fields = (
            "id",

            "evenement",

            "corps",
            "grade",
            "classe",
            "echelon",

            "structure",

            "date_recrutement",

            "created_at",
            "updated_at",
        )


class RecrutementReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des recrutements.
    """

    evenement = EvenementCarriereReadSerializer(
        read_only=True
    )

    corps = CorpsReadSerializer(
        read_only=True
    )

    grade = GradeReadSerializer(
        read_only=True
    )

    classe = ClasseReadSerializer(
        read_only=True
    )

    echelon = EchelonReadSerializer(
        read_only=True
    )

    structure = StructureReadSerializer(
        read_only=True
    )

    class Meta:
        model = Recrutement

        fields = (
            "id",

            "evenement",

            "corps",
            "grade",
            "classe",
            "echelon",

            "structure",

            "date_recrutement",

            "created_at",
            "updated_at",
        )