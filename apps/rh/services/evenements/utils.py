# apps/rh/services/evenements/utils.py

"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/evenements/utils.py

Description :
    Fabrique des objets métier du moteur
    de carrière.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.models.affectation import Affectation
from apps.rh.models.agent import SituationAdministrative
from apps.rh.models.occupation import OccupationPoste


# ==========================================================
# Situation administrative
# ==========================================================

def creer_situation(
    *,
    agent,
    source,
    date_effet,
    evenement,
):
    """
    Crée une nouvelle situation administrative
    à partir d'un objet métier.

    Le paramètre source peut être :

        - Recrutement
        - Titularisation
        - Nomination
        - Reclassement
    """

    return SituationAdministrative.objects.create(

        agent=agent,

        motif=source.motif,

        corps=source.corps,

        grade=source.grade,

        classe=source.classe,

        echelon=source.echelon,

        position_administrative=(
            source.position_administrative
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

    situation.date_fin = date_fin

    situation.est_courante = False

    situation.save(
        update_fields=[
            "date_fin",
            "est_courante",
            "updated_at",
        ]
    )


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

        structure=source.structure,

        unite=source.unite,

        poste=source.poste,

        date_prise_service=(
            source.date_prise_service
        ),

        evenement=evenement,

        est_courante=True,
    )


def cloturer_affectation(
    affectation,
    date_fin,
):
    """
    Clôture une affectation.
    """

    affectation.date_fin = date_fin

    affectation.est_courante = False

    affectation.save(
        update_fields=[
            "date_fin",
            "est_courante",
            "updated_at",
        ]
    )


# ==========================================================
# Occupation de poste
# ==========================================================

def creer_occupation(
    *,
    agent,
    source,
    evenement,
):
    """
    Crée une nouvelle occupation de poste.

    Retourne None lorsqu'aucun poste
    n'est renseigné.
    """

    if not source.poste:
        return None

    return OccupationPoste.objects.create(

        agent=agent,

        poste=source.poste,

        evenement=evenement,

        date_debut=source.date_prise_service,
    )


def cloturer_occupation(
    occupation,
    date_fin,
):
    """
    Clôture une occupation de poste.
    """

    if occupation is None:
        return

    occupation.date_fin = date_fin

    occupation.save(
        update_fields=[
            "date_fin",
            "updated_at",
        ]
    )