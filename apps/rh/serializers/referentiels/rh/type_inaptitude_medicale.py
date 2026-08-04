"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/referentiels/rh/type_inaptitude_medicale.py

Description :
    Serializers du référentiel des types d'inaptitude
    médicale.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import serializers

from apps.rh.models.referentiels import (
    TypeInaptitudeMedicale,
)


class TypeInaptitudeMedicaleSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la création
    et la modification des types
    d'inaptitude médicale.
    """

    class Meta:
        model = TypeInaptitudeMedicale

        fields = "__all__"


class TypeInaptitudeMedicaleReadSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la consultation
    des types d'inaptitude médicale.
    """

    class Meta:
        model = TypeInaptitudeMedicale

        fields = "__all__"