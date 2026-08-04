# apps/rh/services/evenements/utils.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/utils.py

Description :
    Fonctions utilitaires du moteur de carrière.

Auteur : SGCP
Version : 2.1
==========================================================
"""

from apps.rh.models.affectation import Affectation
from apps.rh.models.carriere import SituationAdministrative
from apps.rh.models.occupation import OccupationPoste


# ==========================================================
# Situation administrative
# ==========================================================

def creer_situation(
    *,
    agent,
    source,
    evenement,
    date_effet,
    situation_courante=None,
):
    """
    Crée une nouvelle situation administrative.

    Les informations absentes de la fiche
    spécialisée sont reprises de la situation
    courante lorsqu'elle existe.
    """

    return SituationAdministrative.objects.create(

        agent=agent,

        corps=(
            getattr(source, "corps", None)
            or (
                situation_courante.corps
                if situation_courante
                else None
            )
        ),

        grade=(
            getattr(source, "grade", None)
            or (
                situation_courante.grade
                if situation_courante
                else None
            )
        ),

        classe=(
            getattr(source, "classe", None)
            or (
                situation_courante.classe
                if situation_courante
                else None
            )
        ),

        echelon=(
            getattr(source, "echelon", None)
            or (
                situation_courante.echelon
                if situation_courante
                else None
            )
        ),

        position_administrative=(
            getattr(source, "position_administrative", None)

            or evenement.position_administrative

            or (
                situation_courante.position_administrative
                if situation_courante
                else None
            )
        ),

        date_effet=date_effet,

        evenement=evenement,

        est_courante=True,
    )


def cloturer_situation(
    situation,
    date_fin,
):
    """
    Clôture une situation administrative.
    """

    if situation is None:
        return None

    situation.date_fin = date_fin

    situation.est_courante = False

    situation.save(
        update_fields=[
            "date_fin",
            "est_courante",
            "updated_at",
        ]
    )

    return situation


# ==========================================================
# Affectation
# ==========================================================

def creer_affectation(
    *,
    agent,
    source,
    evenement,
):
    """
    Crée une nouvelle affectation.
    """

    return Affectation.objects.create(

        agent=agent,

        structure=getattr(source, "structure", None),

        unite=getattr(source, "unite", None),

        poste=getattr(source, "poste", None),

        date_prise_service=getattr(
            source,
            "date_prise_service",
            None,
        ),

        evenement=evenement,

        est_courante=False,
    )


def cloturer_affectation(
    affectation,
):
    """
    Clôture une affectation.
    """

    if affectation is None:
        return None

    affectation.est_courante = False

    affectation.save(
        update_fields=[
            "est_courante",
            "updated_at",
        ]
    )

    return affectation


# ==========================================================
# Occupation de poste
# ==========================================================

def creer_occupation(
    *,
    agent,
    poste,
    evenement,
    date_debut,
    date_fin=None,
    est_interim=False,
):
    """
    Crée une nouvelle occupation de poste.

    Retourne None lorsqu'aucun poste
    n'est fourni.
    """

    if poste is None:
        return None

    return OccupationPoste.objects.create(

        agent=agent,

        poste=poste,

        evenement=evenement,

        date_debut=date_debut,

        date_fin=date_fin,

        est_interim=est_interim,
    )


def cloturer_occupation(
    occupation,
    date_fin,
):
    """
    Clôture une occupation de poste.
    """

    if occupation is None:
        return None

    occupation.date_fin = date_fin

    occupation.save(
        update_fields=[
            "date_fin",
            "updated_at",
        ]
    )

    return occupation


# ==========================================================
# Lecture des données courantes
# ==========================================================

def get_affectation_courante(agent):
    """
    Retourne l'affectation courante de l'agent.
    """

    return (
        Affectation.objects.filter(
            agent=agent,
            est_courante=True,
        )
        .select_related(
            "structure",
            "unite",
            "poste",
        )
        .first()
    )


def get_occupation_active(poste):
    """
    Retourne l'occupation active d'un poste.

    Une occupation active peut être
    le titulaire ou un intérimaire.
    """

    return (
        OccupationPoste.objects.filter(
            poste=poste,
            date_fin__isnull=True,
        )
        .select_related(
            "agent",
            "poste",
            "evenement",
        )
        .first()
    )


def get_interim_actif(agent):
    """
    Retourne l'intérim actif assuré par l'agent.
    """

    return (
        OccupationPoste.objects.filter(
            agent=agent,
            est_interim=True,
            date_fin__isnull=True,
        )
        .select_related(
            "poste",
            "evenement",
        )
        .first()
    )