from rest_framework import serializers

from apps.rh.models import Reclassement
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.referentiels import (
    Classe,
    Corps,
    Echelon,
    Grade,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)
from apps.rh.serializers.referentiels.statut.classe import (
    ClasseReadSerializer,
)
from apps.rh.serializers.referentiels.statut.echelon import (
    EchelonReadSerializer,
)
from apps.rh.serializers.referentiels.statut.grade import (
    GradeReadSerializer,
)


class ReclassementSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des fiches spécialisées de reclassement.
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

    class Meta:
        model = Reclassement

        fields = (
            "id",

            "evenement",

            "corps",
            "grade",
            "classe",
            "echelon",

            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class ReclassementReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des fiches spécialisées de reclassement.
    """

    evenement = EvenementCarriereReadSerializer(
        read_only=True
    )

    corps = serializers.PrimaryKeyRelatedField(
        queryset=Corps.objects.filter(actif=True)
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

    class Meta:
        model = Reclassement

        fields = (
            "id",

            "evenement",

            "corps",
            "grade",
            "classe",
            "echelon",

            "created_at",
            "updated_at",
        )