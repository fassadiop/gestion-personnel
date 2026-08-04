"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/type_inaptitude_medicale.py

Description :
    ViewSet du référentiel des types
    d'inaptitude médicale.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.views.base import (
    BaseViewSet,
)

from apps.rh.models.referentiels import (
    TypeInaptitudeMedicale,
)

from apps.rh.serializers.referentiels.rh.type_inaptitude_medicale import (
    TypeInaptitudeMedicaleSerializer,
    TypeInaptitudeMedicaleReadSerializer,
)


class TypeInaptitudeMedicaleViewSet(
    BaseViewSet,
):
    """
    API de gestion du référentiel
    des types d'inaptitude médicale.
    """

    queryset = (
        TypeInaptitudeMedicale.objects
        .all()
    )

    serializer_class = (
        TypeInaptitudeMedicaleSerializer
    )

    read_serializer_class = (
        TypeInaptitudeMedicaleReadSerializer
    )

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )