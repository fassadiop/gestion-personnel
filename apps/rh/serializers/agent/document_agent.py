from rest_framework import serializers

from apps.rh.models import (
    Agent,
    DocumentAgent,
)
from apps.rh.models.organisation import Structure
from apps.rh.models.referentiels import (
    TypeDocument,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)
from apps.rh.serializers.referentiels.document.type_document import (
    TypeDocumentReadSerializer,
)


class DocumentAgentSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la création et la modification
    des documents permanents du dossier de l'agent.
    """

    agent = serializers.PrimaryKeyRelatedField(
        queryset=Agent.objects.filter(actif=True)
    )

    type_document = serializers.PrimaryKeyRelatedField(
        queryset=TypeDocument.objects.filter(actif=True)
    )

    class Meta:
        model = DocumentAgent

        fields = (
            "id",

            "agent",
            "type_document",

            "numero_document",
            "date_document",
            "date_expiration",

            "fichier",

            "nom_fichier",
            "extension",
            "taille",
            "mime_type",
            "hash_document",

            "description",

            "est_verifie",

            "created_at",
            "updated_at",
        )

        read_only_fields = (

            "nom_fichier",
            "extension",
            "taille",
            "mime_type",
            "hash_document",

            "est_verifie",

            "created_at",
            "updated_at",
        )


class DocumentAgentReadSerializer(serializers.ModelSerializer):
    """
    Serializer utilisé pour la consultation
    des documents permanents du dossier de l'agent.
    """

    agent = AgentReadSerializer(
        read_only=True
    )

    type_document = TypeDocumentReadSerializer(
        read_only=True
    )

    verifie_par = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:
        model = DocumentAgent

        fields = (
            "id",

            "agent",
            "type_document",

            "numero_document",
            "date_document",
            "date_expiration",

            "fichier",

            "nom_fichier",
            "extension",
            "taille",
            "mime_type",
            "hash_document",

            "texte_ocr",
            "description",

            "est_verifie",
            "date_verification",
            "verifie_par",

            "created_at",
            "updated_at",
        )