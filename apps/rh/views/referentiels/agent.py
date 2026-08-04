"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/sexe.py

Description :
    ViewSet des sexes.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.views.base import BaseViewSet

from apps.rh.models import StatutAgent

from apps.rh.serializers.referentiels.agent import (
    StatutAgentSerializer,
    StatutAgentReadSerializer,
)

from apps.rh.models import EtatCivil

from apps.rh.serializers.referentiels.agent import (
    EtatCivilSerializer,
    EtatCivilReadSerializer,
)

from apps.rh.models import Sexe

from apps.rh.serializers.referentiels.agent import (
    SexeSerializer,
    SexeReadSerializer,
)

from apps.rh.models import Nationalite

from apps.rh.serializers.referentiels.agent import (
    NationaliteSerializer,
    NationaliteReadSerializer,
)


class SexeViewSet(BaseViewSet):
    """
    ViewSet des sexes.
    """

    queryset = Sexe.objects.all()

    serializer_class = SexeSerializer

    read_serializer_class = SexeReadSerializer

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )


"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/etat_civil.py

Description :
    ViewSet des états civils.

Auteur : SGCP
Version : 1.0
==========================================================
"""


class EtatCivilViewSet(BaseViewSet):
    """
    ViewSet des états civils.
    """

    queryset = EtatCivil.objects.all()

    serializer_class = EtatCivilSerializer

    read_serializer_class = EtatCivilReadSerializer

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )


"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/nationalite.py

Description :
    ViewSet des nationalités.

Auteur : SGCP
Version : 1.0
==========================================================
"""


class NationaliteViewSet(BaseViewSet):
    """
    ViewSet des nationalités.
    """

    queryset = Nationalite.objects.all()

    serializer_class = NationaliteSerializer

    read_serializer_class = NationaliteReadSerializer

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )


"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/referentiels/statut_agent.py

Description :
    ViewSet des statuts d'agent.

Auteur : SGCP
Version : 1.0
==========================================================
"""


class StatutAgentViewSet(BaseViewSet):
    """
    ViewSet des statuts d'agent.
    """

    queryset = StatutAgent.objects.all()

    serializer_class = StatutAgentSerializer

    read_serializer_class = StatutAgentReadSerializer

    search_fields = (
        "code",
        "libelle",
    )

    ordering = (
        "libelle",
    )