# apps/rh/serializers/consultation/statistiques/statistiques.py

from rest_framework import serializers

from .repartition import RepartitionSerializer


class EffectifsStatistiquesSerializer(serializers.Serializer):
    """
    Statistiques globales des effectifs.
    """

    total_agents = serializers.IntegerField()
    agents_actifs = serializers.IntegerField()

    par_sexe = RepartitionSerializer(many=True)
    par_statut = RepartitionSerializer(many=True)
    par_position_administrative = RepartitionSerializer(many=True)


class RepartitionAdministrativeSerializer(serializers.Serializer):
    """
    Répartition des agents par référentiel RH.
    """

    par_corps = RepartitionSerializer(many=True)
    par_grade = RepartitionSerializer(many=True)
    par_classe = RepartitionSerializer(many=True)
    par_echelon = RepartitionSerializer(many=True)


class RepartitionOrganisationnelleSerializer(serializers.Serializer):
    """
    Répartition des agents par organisation.
    """

    par_structure = RepartitionSerializer(many=True)
    par_unite = RepartitionSerializer(many=True)
    par_poste = RepartitionSerializer(many=True)


class MouvementsCarriereSerializer(serializers.Serializer):
    """
    Statistiques des mouvements de carrière.
    """

    total = serializers.IntegerField()

    par_type = RepartitionSerializer(
        many=True,
    )


class StatistiquesTypeSerializer(serializers.Serializer):
    """
    Bloc statistique comportant un total et une répartition.
    """

    total = serializers.IntegerField()

    par_type = RepartitionSerializer(
        many=True,
    )


class CongesAbsencesSerializer(serializers.Serializer):
    """
    Statistiques des congés et absences.
    """

    decisions_conge = StatistiquesTypeSerializer()
    conges = StatistiquesTypeSerializer()
    absences = StatistiquesTypeSerializer()


class StatistiquesSerializer(serializers.Serializer):
    """
    Serializer principal des statistiques du dashboard.
    """

    effectifs = EffectifsStatistiquesSerializer()

    repartition_administrative = (
        RepartitionAdministrativeSerializer()
    )

    repartition_organisationnelle = (
        RepartitionOrganisationnelleSerializer()
    )

    mouvements_carriere = (
        MouvementsCarriereSerializer()
    )

    conges_absences = (
        CongesAbsencesSerializer()
    )