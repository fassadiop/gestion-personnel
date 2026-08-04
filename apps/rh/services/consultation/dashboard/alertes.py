from datetime import timedelta

from django.utils import timezone

from apps.rh.models import (
    Conge,
    Disponibilite,
    Detachement,
    Interim,
    MiseADisposition,
)


class DashboardAlerteService:
    """
    Service de construction des alertes RH.
    """

    DELAI_ALERTE_JOURS = 30

    @classmethod
    def execute(cls):
        return {
            "interims": cls.interims(),
            "detachements": cls.detachements(),
            "mises_disposition": cls.mises_disposition(),
            "disponibilites": cls.disponibilites(),
            "conges": cls.conges(),
        }

    @classmethod
    def _periode_alerte(cls):
        aujourd_hui = timezone.localdate()
        return aujourd_hui, aujourd_hui + timedelta(
            days=cls.DELAI_ALERTE_JOURS
        )

    @classmethod
    def interims(cls):
        aujourd_hui, date_limite = cls._periode_alerte()

        return (
            Interim.objects
            .filter(
                evenement__date_fin__gte=aujourd_hui,
                evenement__date_fin__lte=date_limite,
            )
            .select_related(
                "evenement__agent",
                "poste",
            )
            .order_by("evenement__date_fin")
        )

    @classmethod
    def detachements(cls):
        aujourd_hui, date_limite = cls._periode_alerte()

        return (
            Detachement.objects
            .filter(
                date_fin__gte=aujourd_hui,
                date_fin__lte=date_limite,
            )
            .select_related(
                "evenement__agent",
                "structure",
                "unite",
            )
            .order_by("date_fin")
        )

    @classmethod
    def mises_disposition(cls):
        aujourd_hui, date_limite = cls._periode_alerte()

        return (
            MiseADisposition.objects
            .filter(
                date_fin__gte=aujourd_hui,
                date_fin__lte=date_limite,
            )
            .select_related(
                "evenement__agent",
                "structure",
                "unite",
            )
            .order_by("date_fin")
        )

    @classmethod
    def disponibilites(cls):
        aujourd_hui, date_limite = cls._periode_alerte()

        return (
            Disponibilite.objects
            .filter(
                date_fin__gte=aujourd_hui,
                date_fin__lte=date_limite,
            )
            .select_related(
                "evenement__agent",
            )
            .order_by("date_fin")
        )

    @classmethod
    def conges(cls):
        aujourd_hui, date_limite = cls._periode_alerte()

        return (
            Conge.objects
            .filter(
                date_reprise__gte=aujourd_hui,
                date_reprise__lte=date_limite,
            )
            .select_related(
                "evenement__agent",
                "decision_conge",
            )
            .order_by("date_reprise")
        )