from rest_framework import serializers

from apps.rh.models.documents import DocumentAdministratif
from apps.rh.models.evenement import EvenementCarriere
from apps.rh.models.organisation import Structure
from apps.rh.models.referentiels import TypeDocument

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)
from apps.rh.serializers.organisation.structure import (
    StructureReadSerializer,
)
from apps.rh.serializers.referentiels.document.type_document import (
    TypeDocumentReadSerializer,
)


class DocumentSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des documents administratifs.
    """

    evenement = serializers.PrimaryKeyRelatedField(
        queryset=EvenementCarriere.objects.filter(actif=True)
    )

    type_document = serializers.PrimaryKeyRelatedField(
        queryset=TypeDocument.objects.filter(actif=True)
    )

    structure_emettrice = serializers.PrimaryKeyRelatedField(
        queryset=Structure.objects.filter(actif=True)
    )

    class Meta:
        model = DocumentAdministratif

        fields = (
            "id",

            "evenement",
            "type_document",
            "structure_emettrice",

            "numero_document",
            "date_document",
            "signataire",

            "fichier",
            "nom_fichier",
            "taille",
            "extension",
            "mime_type",
            "hash_document",

            "description",

            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "nom_fichier",
            "taille",
            "extension",
            "mime_type",
            "hash_document",
            "created_at",
            "updated_at",
        )


class DocumentReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des documents administratifs.
    """

    evenement = EvenementCarriereReadSerializer(
        read_only=True
    )

    type_document = TypeDocumentReadSerializer(
        read_only=True
    )

    structure_emettrice = StructureReadSerializer(
        read_only=True
    )

    class Meta:
        model = DocumentAdministratif

        fields = (
            "id",

            "evenement",
            "type_document",
            "structure_emettrice",

            "numero_document",
            "date_document",
            "signataire",

            "fichier",
            "nom_fichier",
            "taille",
            "extension",
            "mime_type",
            "hash_document",
            "texte_ocr",

            "description",

            "created_at",
            "updated_at",
        )