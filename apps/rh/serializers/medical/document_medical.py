from rest_framework import serializers

from apps.rh.models import (
    DocumentMedical,
    DossierMedical,
)
from apps.rh.models.referentiels import (
    TypeDocumentMedical,
)

from apps.rh.serializers.medical.dossier_medical import (
    DossierMedicalReadSerializer,
)
from apps.rh.serializers.referentiels.document.type_document_medical import (
    TypeDocumentMedicalReadSerializer,
)


class DocumentMedicalSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des documents médicaux.
    """

    dossier_medical = serializers.PrimaryKeyRelatedField(
        queryset=DossierMedical.objects.filter(actif=True)
    )

    type_document = serializers.PrimaryKeyRelatedField(
        queryset=TypeDocumentMedical.objects.filter(actif=True)
    )

    class Meta:
        model = DocumentMedical

        fields = (
            "id",

            "dossier_medical",
            "type_document",

            "date_document",
            "numero_document",

            "fichier",
            "nom_original",
            "taille",
            "extension",
            "mime_type",
            "hash_document",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )


class DocumentMedicalReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des documents médicaux.
    """

    dossier_medical = DossierMedicalReadSerializer(
        read_only=True
    )

    type_document = (
        TypeDocumentMedicalReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = DocumentMedical

        fields = (
            "id",

            "dossier_medical",
            "type_document",

            "date_document",
            "numero_document",

            "fichier",
            "nom_original",
            "taille",
            "extension",
            "mime_type",
            "hash_document",

            "observation",
            "actif",

            "created_at",
            "updated_at",
        )