# apps/rh/serializers/inaptitude_medicale/inaptitude_medicale.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/inaptitude_medicale/inaptitude_medicale.py

Description :
    Serializers de l'inaptitude médicale.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import serializers

from apps.rh.models.inaptitude_medicale import (
    InaptitudeMedicale,
)

from apps.rh.models.referentiels import (
    TypeInaptitudeMedicale,
)

from apps.rh.serializers.agent.agent import (
    AgentReadSerializer,
)

from apps.rh.serializers.evenement.evenement import (
    EvenementCarriereReadSerializer,
)
from apps.rh.serializers.referentiels.rh.type_inaptitude_medicale import TypeInaptitudeMedicaleReadSerializer




class InaptitudeMedicaleSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la création
    et la modification des inaptitudes médicales.
    """

    type_inaptitude = serializers.PrimaryKeyRelatedField(
        queryset=TypeInaptitudeMedicale.objects.all(),
    )

    class Meta:
        model = InaptitudeMedicale

        fields = (
            "id",

            "type_inaptitude",

            "date_effet",

            "date_fin",

            "observation",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )


class InaptitudeMedicaleReadSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer utilisé pour la consultation
    des inaptitudes médicales.
    """

    evenement = (
        EvenementCarriereReadSerializer(
            read_only=True,
        )
    )

    agent = AgentReadSerializer(
        source="evenement.agent",
        read_only=True,
    )

    type_inaptitude = (
        TypeInaptitudeMedicaleReadSerializer(
            read_only=True,
        )
    )

    class Meta:
        model = InaptitudeMedicale

        fields = (
            "id",

            "evenement",

            "agent",

            "type_inaptitude",

            "date_effet",

            "date_fin",

            "observation",

            "created_at",

            "updated_at",
        )

        read_only_fields = (
            "created_at",
            "updated_at",
        )