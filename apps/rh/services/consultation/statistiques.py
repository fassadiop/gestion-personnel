from django.db.models import Count, F

from apps.rh.models import (
    Absence,
    Affectation,
    Agent,
    Conge,
    EvenementCarriere,
)
from apps.rh.models.carriere import SituationAdministrative


class StatistiquesService:
    """
    Service de statistiques RH agrégées.

    Fournit une vue statistique globale :
    - effectifs ;
    - répartition administrative ;
    - répartition organisationnelle ;
    - mouvements de carrière ;
    - congés et absences.
    """

    @classmethod
    def execute(cls):
        situations = SituationAdministrative.objects.filter(
            est_courante=True,
        )

        affectations = Affectation.objects.filter(
            est_courante=True,
        )

        return {
            "effectifs": {
                "total": Agent.objects.count(),

                "par_sexe": list(
                    Agent.objects
                    .values(
                        code=F("sexe__code"),
                        libelle=F("sexe__libelle"),
                    )
                    .annotate(
                        nombre=Count("id")
                    )
                    .order_by("libelle")
                ),

                "par_statut": list(
                    Agent.objects
                    .values(
                        code=F("statut__code"),
                        libelle=F("statut__libelle"),
                    )
                    .annotate(
                        nombre=Count("id")
                    )
                    .order_by("libelle")
                ),

                "par_position_administrative": list(
                    situations
                    .values(
                        code=F(
                            "position_administrative__code"
                        ),
                        libelle=F(
                            "position_administrative__libelle"
                        ),
                    )
                    .annotate(
                        nombre=Count("id")
                    )
                    .order_by("libelle")
                ),
            },

            "repartition_administrative": {
                "par_corps": list(
                    situations
                    .values(
                        code=F("corps__code"),
                        libelle=F("corps__libelle"),
                    )
                    .annotate(
                        nombre=Count("id")
                    )
                    .order_by("libelle")
                ),

                "par_grade": list(
                    situations
                    .values(
                        code=F("grade__code"),
                        libelle=F("grade__libelle"),
                    )
                    .annotate(
                        nombre=Count("id")
                    )
                    .order_by("libelle")
                ),

                "par_classe": list(
                    situations
                    .values(
                        code=F("classe__code"),
                        libelle=F("classe__libelle"),
                    )
                    .annotate(
                        nombre=Count("id")
                    )
                    .order_by("libelle")
                ),

                "par_echelon": list(
                    situations
                    .values(
                        code=F("echelon__code"),
                        libelle=F("echelon__libelle"),
                    )
                    .annotate(
                        nombre=Count("id")
                    )
                    .order_by("libelle")
                ),
            },

            "repartition_organisationnelle": {
                "par_structure": list(
                    affectations
                    .values(
                        code=F("structure__code"),
                        libelle=F("structure__nom"),
                    )
                    .annotate(
                        nombre=Count("id")
                    )
                    .order_by("libelle")
                ),

                "par_unite": list(
                    affectations
                    .values(
                        code=F("unite__code"),
                        libelle=F("unite__nom"),
                    )
                    .annotate(
                        nombre=Count("id")
                    )
                    .order_by("libelle")
                ),
            },

            "mouvements_carriere": {
                "par_type_evenement": list(
                    EvenementCarriere.objects
                    .values(
                        code=F("type_evenement__code"),
                        libelle=F(
                            "type_evenement__libelle"
                        ),
                    )
                    .annotate(
                        nombre=Count("id")
                    )
                    .order_by("libelle")
                ),
            },

            "conges_absences": {
                "conges_par_type": list(
                    Conge.objects
                    .values(
                        code=F(
                            "decision_conge__type_conge__code"
                        ),
                        libelle=F(
                            "decision_conge__type_conge__libelle"
                        ),
                    )
                    .annotate(
                        nombre=Count("id")
                    )
                    .order_by("libelle")
                ),

                "absences": {
                    "nombre": Absence.objects.count(),

                    "nombre_jours": sum(
                        absence.nombre_jours
                        for absence
                        in Absence.objects.all()
                    ),
                },
            },
        }