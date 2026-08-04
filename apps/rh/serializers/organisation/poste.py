from rest_framework import serializers

from apps.rh.models.organisation import (
    Poste,
    Structure,
    UniteOrganisationnelle,
)
from apps.rh.models.referentiels import Hierarchie
from apps.rh.serializers.organisation.structure import StructureReadSerializer
from apps.rh.serializers.referentiels.statut.hierarchie import HierarchieReadSerializer

from .unite_organisationnelle import (
    UniteOrganisationnelleReadSerializer,
)


class PosteSerializer(serializers.ModelSerializer):

    structure = serializers.PrimaryKeyRelatedField(
        queryset=Structure.objects.filter(actif=True)
    )

    unite = serializers.PrimaryKeyRelatedField(
        queryset=UniteOrganisationnelle.objects.filter(actif=True),
        allow_null=True,
        required=False,
    )

    hierarchie_minimale = serializers.PrimaryKeyRelatedField(
        queryset=Hierarchie.objects.filter(actif=True),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Poste

        fields = (
            "id",
            "structure",
            "unite",
            "code",
            "libelle",
            "description",
            "hierarchie_minimale",
            "est_responsable",
            "est_budgetise",
            "actif",
            "created_at",
            "updated_at",
        )

    def validate(self, attrs):
        structure = attrs.get("structure")
        unite = attrs.get("unite")
        code = attrs.get("code")
        libelle = attrs.get("libelle")

        # Vérifie que l'unité appartient à la structure
        if unite and unite.structure != structure:
            raise serializers.ValidationError(
                {
                    "unite": (
                        "L'unité organisationnelle sélectionnée "
                        "n'appartient pas à cette structure."
                    )
                }
            )

        # Vérifie l'unicité du code dans la structure
        queryset = Poste.objects.filter(
            structure=structure,
            code=code,
        )

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                {
                    "code": (
                        "Un poste portant ce code existe déjà "
                        "dans cette structure."
                    )
                }
            )

        # Vérifie l'unicité du libellé dans l'unité
        if unite:
            queryset = Poste.objects.filter(
                unite=unite,
                libelle=libelle,
            )

            if self.instance:
                queryset = queryset.exclude(pk=self.instance.pk)

            if queryset.exists():
                raise serializers.ValidationError(
                    {
                        "libelle": (
                            "Un poste portant ce libellé existe déjà "
                            "dans cette unité."
                        )
                    }
                )

        return attrs


class PosteReadSerializer(serializers.ModelSerializer):

    structure = StructureReadSerializer(
        read_only=True
    )

    unite = UniteOrganisationnelleReadSerializer(
        read_only=True
    )

    hierarchie_minimale = HierarchieReadSerializer(
        read_only=True
    )

    class Meta:
        model = Poste

        fields = (
            "id",
            "structure",
            "unite",
            "code",
            "libelle",
            "description",
            "hierarchie_minimale",
            "est_responsable",
            "est_budgetise",
            "actif",
            "created_at",
            "updated_at",
        )

    