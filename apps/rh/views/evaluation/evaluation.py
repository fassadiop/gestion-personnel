"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : views/evaluation/evaluation.py

Description :
    ViewSet des évaluations.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models import (
    Evaluation,
)

from apps.rh.serializers.evaluation.evaluation import (
    EvaluationSerializer,
    EvaluationReadSerializer,
)

from apps.rh.views.base import BaseViewSet


class EvaluationViewSet(
    BaseViewSet
):
    """
    ViewSet des évaluations.
    """

    queryset = (
        Evaluation.objects.all()
    )

    serializer_class = (
        EvaluationSerializer
    )

    read_serializer_class = (
        EvaluationReadSerializer
    )

    search_fields = (
        "agent__matricule",
        "agent__nom",
        "agent__prenom",
        "evaluateur__nom",
        "evaluateur__prenom",
        "unite_organisationnelle__nom",
    )

    ordering = (
        "-annee",
        "-date_evaluation",
    )

    select_related_fields = (
        "agent",
        "evaluateur",
        "unite_organisationnelle",
        "evenement_carriere",
    )