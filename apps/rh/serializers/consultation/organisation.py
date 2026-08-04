from rest_framework import serializers


class TypeOrganisationSerializer(serializers.Serializer):
    """
    Représentation simplifiée d'un type
    de structure ou d'unité.
    """

    code = serializers.CharField()
    libelle = serializers.CharField()


class PosteOrganisationSerializer(serializers.Serializer):
    """
    Représentation d'un poste dans l'organigramme.
    """

    id = serializers.IntegerField()
    code = serializers.CharField()
    libelle = serializers.CharField()

    est_responsable = serializers.BooleanField()
    est_budgetise = serializers.BooleanField()

    hierarchie_minimale = serializers.CharField(
        allow_null=True,
    )


class UniteOrganisationTreeSerializer(serializers.Serializer):
    """
    Représentation récursive d'une unité organisationnelle.
    """

    id = serializers.IntegerField()
    code = serializers.CharField()
    sigle = serializers.CharField(
        allow_blank=True,
    )
    nom = serializers.CharField()
    ordre = serializers.IntegerField()

    type_unite = TypeOrganisationSerializer()

    responsable = serializers.CharField(
        allow_null=True,
    )

    postes = PosteOrganisationSerializer(
        many=True,
    )

    enfants = serializers.SerializerMethodField()

    def get_enfants(self, obj):
        return UniteOrganisationTreeSerializer(
            obj.get("enfants", []),
            many=True,
        ).data


class StructureOrganisationTreeSerializer(
    serializers.Serializer
):
    """
    Représentation d'une structure et de son
    arborescence organisationnelle complète.
    """

    id = serializers.IntegerField()
    code = serializers.CharField()
    sigle = serializers.CharField()
    nom = serializers.CharField()

    type_structure = TypeOrganisationSerializer()

    postes = PosteOrganisationSerializer(
        many=True,
    )

    unites = UniteOrganisationTreeSerializer(
        many=True,
    )


class OrganisationTreeSerializer(serializers.Serializer):
    """
    Serializer racine de l'organigramme.
    """

    structures = StructureOrganisationTreeSerializer(
        many=True,
    )