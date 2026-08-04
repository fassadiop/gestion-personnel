# apps/administration/serializers/profil_administration.py

from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.administration.models.profil_administration import (
    ProfilAdministration,
)
from apps.rh.models.organisation import Structure
from apps.rh.serializers.organisation.structure import (
    StructureReadSerializer,
)

User = get_user_model()


class ProfilAdministrationSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification d'un profil
    d'administration.
    """

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )

    structure_racine = serializers.PrimaryKeyRelatedField(
        queryset=Structure.objects.filter(
            actif=True,
            parent__isnull=True,
        ),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = ProfilAdministration

        fields = (
            "id",
            "user",
            "structure_racine",
            "actif",
            "created_at",
            "updated_at",
        )


class ProfilAdministrationReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    d'un profil d'administration.
    """

    user = serializers.StringRelatedField(
        read_only=True
    )

    structure_racine = (
        StructureReadSerializer(
            read_only=True
        )
    )

    class Meta:
        model = ProfilAdministration

        fields = (
            "id",
            "user",
            "structure_racine",
            "actif",
            "created_at",
            "updated_at",
        )