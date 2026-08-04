"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/rh/type_mouvement_conge.py

Description :
    Serializers du référentiel des types
    de mouvements de congé.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import serializers

from apps.rh.models import (
    TypeMouvementConge,
)


class TypeMouvementCongeSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la création
    et la modification des types
    de mouvements de congé.
    """

    class Meta:
        model = TypeMouvementConge

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "sens",

            "actif",

            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class TypeMouvementCongeReadSerializer(
    serializers.ModelSerializer
):
    """
    Serializer utilisé pour la consultation
    des types de mouvements de congé.
    """

    class Meta:
        model = TypeMouvementConge

        fields = (
            "id",

            "code",
            "libelle",
            "description",

            "sens",

            "actif",

            "created_at",
            "updated_at",
        )