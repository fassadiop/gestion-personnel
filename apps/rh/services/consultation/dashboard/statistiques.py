from django.db.models import Count, QuerySet
from typing import Any
from apps.rh.models.absence import Absence
from apps.rh.models.affectation import Affectation
from apps.rh.models.agent import Agent
from apps.rh.models.carriere import SituationAdministrative
from apps.rh.models.conges import Conge
from apps.rh.models.decision_conge import DecisionConge
from apps.rh.models.evenement import EvenementCarriere

class DashboardStatistiquesService:
    """
    Service de production des statistiques du tableau de bord RH.
    """

    @classmethod
    def execute(cls):
        """
        Retourne l'ensemble des statistiques du tableau de bord.
        """

        return {
            "effectifs": cls.effectifs(),
            "repartition_administrative": cls.repartition_administrative(),
            "repartition_organisationnelle": cls.repartition_organisationnelle(),
            "mouvements_carriere": cls.mouvements_carriere(),
            "conges_absences": cls.conges_absences(),
        }


    @classmethod
    def effectifs(cls):
        """
        Statistiques globales des effectifs.
        """

        agents = Agent.objects.filter(actif=True)

        situations = (
            SituationAdministrative.objects
            .filter(
                actif=True,
                date_fin__isnull=True,
            )
            .select_related(
                "position_administrative",
            )
        )

        return {
            "total_agents": Agent.objects.count(),
            "agents_actifs": Agent.objects.filter(actif=True).count(),
            "par_sexe": cls._repartition(
                queryset=agents,
                code_field="sexe__code",
                libelle_field="sexe__libelle",
            ),
            "par_statut": cls._repartition(
                queryset=agents,
                code_field="statut__code",
                libelle_field="statut__libelle",
            ),
            "par_position_administrative": cls._repartition(
                queryset=situations,
                code_field="position_administrative__code",
                libelle_field="position_administrative__libelle",
            ),
        }

    @classmethod
    def repartition_administrative(cls):
        """
        Répartition des agents par référentiel RH.
        """

        situations = (
            SituationAdministrative.objects
            .filter(
                actif=True,
                date_fin__isnull=True,
            )
            .select_related(
                "corps",
                "grade",
                "classe",
                "echelon",
            )
        )

        return {
            "par_corps": cls._repartition(
                queryset=situations,
                code_field="corps__code",
                libelle_field="corps__libelle",
            ),
            "par_grade": cls._repartition(
                queryset=situations,
                code_field="grade__code",
                libelle_field="grade__libelle",
            ),
            "par_classe": cls._repartition(
                queryset=situations,
                code_field="classe__code",
                libelle_field="classe__libelle",
            ),
            "par_echelon": cls._repartition(
                queryset=situations,
                code_field="echelon__code",
                libelle_field="echelon__libelle",
            ),
        }

    @classmethod
    def repartition_organisationnelle(cls):
        """
        Répartition des agents par organisation.
        """

        affectations = (
            Affectation.objects
            .filter(
                actif=True,
                est_courante=True,
            )
            .select_related(
                "structure",
                "unite",
                "poste",
            )
        )

        return {
            "par_structure": cls._repartition(
                queryset=affectations,
                code_field="structure__code",
                libelle_field="structure__nom",
            ),
            "par_unite": cls._repartition(
                queryset=affectations,
                code_field="unite__code",
                libelle_field="unite__nom",
            ),
            "par_poste": cls._repartition(
                queryset=affectations,
                code_field="poste__code",
                libelle_field="poste__libelle",
            ),
        }


    @classmethod
    def mouvements_carriere(cls):
        """
        Statistiques des mouvements de carrière.
        """

        evenements = EvenementCarriere.objects.all()

        repartition = (
            evenements
            .values(
                "type_evenement__code",
                "type_evenement__libelle",
            )
            .annotate(nombre=Count("id"))
            .order_by("type_evenement__libelle")
        )

        return {
            "total": evenements.count(),
            "par_type": [
                {
                    "code": ligne["type_evenement__code"],
                    "libelle": ligne["type_evenement__libelle"],
                    "nombre": ligne["nombre"],
                }
                for ligne in repartition
            ],
        }

    @classmethod
    def conges_absences(cls):
        """
        Statistiques des congés et absences.
        """

        return {
            "decisions_conge": {
                "total": DecisionConge.objects.count(),
                "par_type": cls._repartition(
                    queryset=DecisionConge.objects.all(),
                    code_field="type_conge__code",
                    libelle_field="type_conge__libelle",
                ),
            },
            "conges": {
                "total": Conge.objects.count(),
                "par_type": cls._repartition(
                    queryset=Conge.objects.all(),
                    code_field="decision_conge__type_conge__code",
                    libelle_field="decision_conge__type_conge__libelle",
                ),
            },
            "absences": {
                "total": Absence.objects.count(),
                "par_type": cls._repartition(
                    queryset=Absence.objects.all(),
                    code_field="type_absence__code",
                    libelle_field="type_absence__libelle",
                ),
            },
        }


    @staticmethod
    def _repartition(
        queryset: QuerySet,
        *,
        code_field: str,
        libelle_field: str,
        count_field: str = "id",
    ) -> list[dict[str, Any]]:
        """
        Construit une répartition statistique générique.
        """

        relation = code_field.split("__")[0]

        repartition = (
            queryset
            .filter(**{f"{relation}__isnull": False})
            .values(code_field, libelle_field)
            .annotate(nombre=Count(count_field, distinct=True))
            .order_by(libelle_field)
        )

        return [
            {
                "code": ligne[code_field],
                "libelle": ligne[libelle_field],
                "nombre": ligne["nombre"],
            }
            for ligne in repartition
        ]