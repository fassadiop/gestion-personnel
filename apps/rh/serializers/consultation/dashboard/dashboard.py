# apps/rh/serializers/consultation/dashboard/dashboard.py

from rest_framework import serializers

from apps.rh.serializers.consultation.statistiques.statistiques import StatistiquesSerializer

from .alerte_conge import DashboardAlerteCongeSerializer
from .alerte_detachement import DashboardAlerteDetachementSerializer
from .alerte_disponibilite import DashboardAlerteDisponibiliteSerializer
from .alerte_interim import DashboardAlerteInterimSerializer
from .alerte_mise_disposition import DashboardAlerteMiseDispositionSerializer
from .evenement import DashboardEvenementSerializer
from .kpi import DashboardKPISerializer


class DashboardAlerteSerializer(serializers.Serializer):
    interims = DashboardAlerteInterimSerializer(many=True)
    mises_disposition = DashboardAlerteMiseDispositionSerializer(many=True)
    disponibilites = DashboardAlerteDisponibiliteSerializer(many=True)
    conges = DashboardAlerteCongeSerializer(many=True)
    detachements = DashboardAlerteDetachementSerializer(many=True)


class DashboardSerializer(serializers.Serializer):
    kpi = DashboardKPISerializer()

    statistiques = StatistiquesSerializer()

    derniers_evenements = DashboardEvenementSerializer(
        many=True
    )

    alertes = DashboardAlerteSerializer()