"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : services/creation/utils.py

Description :
    Fonctions utilitaires du moteur
    de création des événements.

Auteur : SGCP
Version : 1.1
==========================================================
"""

from apps.rh.models.affectation import Affectation
from apps.rh.models.compteur_conge import CompteurConge
from apps.rh.models.decision_conge import DecisionConge
from apps.rh.models.demission import Demission
from apps.rh.models.detachement import Detachement
from apps.rh.models.disponibilite import Disponibilite
from apps.rh.models.fin_interim import FinInterim
from apps.rh.models.interim import Interim
from apps.rh.models.mise_a_disposition import MiseADisposition
from apps.rh.models.mouvement_compteur_conge import MouvementCompteurConge
from apps.rh.models.nomination import Nomination
from apps.rh.models.radiation import Radiation
from apps.rh.models.reclassement import Reclassement
from apps.rh.models.recrutement import Recrutement
from apps.rh.models.retraite import Retraite
from apps.rh.models.titularisation import Titularisation


# ==========================================================
# Affectation
# ==========================================================

def creer_affectation(
    *,
    evenement,
    agent,
    structure,
    unite=None,
    poste=None,
):
    """
    Crée la fiche spécialisée d'affectation.

    Cette fiche constitue les données
    préparatoires de l'événement.

    Elle n'a aucun effet sur la carrière
    tant que l'événement n'est pas validé.
    """

    return Affectation.objects.create(

        evenement=evenement,

        agent=agent,

        structure_id=structure,

        unite_id=unite,

        poste_id=poste,

        est_courante=False,
    )


# ==========================================================
# Reclassement
# ==========================================================

def creer_reclassement(
    *,
    evenement,
    corps,
    grade,
    classe,
    echelon,
):
    """
    Crée la fiche spécialisée de reclassement.

    Cette fiche constitue les données
    préparatoires de l'événement.

    Elle n'a aucun effet sur la carrière
    tant que l'événement n'est pas validé.
    """

    return Reclassement.objects.create(

        evenement=evenement,

        corps_id=corps,

        grade_id=grade,

        classe_id=classe,

        echelon_id=echelon,
    )

# ==========================================================
# Recrutement
# ==========================================================

def creer_recrutement(
    *,
    evenement,
    corps,
    grade,
    classe,
    echelon,
    structure,
    date_recrutement,
):
    """
    Crée la fiche spécialisée de recrutement.

    Cette fiche constitue les données
    préparatoires de l'événement.

    Elle n'a aucun effet sur la carrière
    tant que l'événement n'est pas validé.
    """

    return Recrutement.objects.create(

        evenement=evenement,

        corps_id=corps,

        grade_id=grade,

        classe_id=classe,

        echelon_id=echelon,

        structure_id=structure,

        date_recrutement=date_recrutement,
    )


# ==========================================================
# Titularisation
# ==========================================================

def creer_titularisation(
    *,
    evenement,
    position_administrative,
    grade,
    classe,
    echelon,
):
    """
    Crée la fiche spécialisée de titularisation.

    Cette fiche constitue les données
    préparatoires de l'événement.

    Elle n'a aucun effet sur la carrière
    tant que l'événement n'est pas validé.
    """

    return Titularisation.objects.create(

        evenement=evenement,

        position_administrative_id=position_administrative,

        grade_id=grade,

        classe_id=classe,

        echelon_id=echelon,
    )

# ==========================================================
# Nomination
# ==========================================================

def creer_nomination(
    *,
    evenement,
    structure,
    unite,
    poste,
):
    """
    Crée la fiche spécialisée de nomination.

    Cette fiche constitue les données
    préparatoires de l'événement.

    Elle n'a aucun effet sur la carrière
    tant que l'événement n'est pas validé.
    """

    nomination = Nomination.objects.create(

        evenement=evenement,

        structure_id=structure,

        unite_id=unite,

        poste_id=poste,
    )

    creer_affectation(

        evenement=evenement,

        agent=evenement.agent,

        structure=structure,

        unite=unite,

        poste=poste,
    )

    return nomination

# ==========================================================
# Intérim
# ==========================================================

def creer_interim(
    *,
    evenement,
    poste,
):
    """
    Crée la fiche spécialisée d'intérim.

    Cette fiche constitue les données
    préparatoires de l'événement.

    Elle n'a aucun effet sur la carrière
    tant que l'événement n'est pas validé.
    """

    return Interim.objects.create(

        evenement=evenement,

        poste_id=poste,
    )

# ==========================================================
# Fin d'intérim
# ==========================================================

def creer_fin_interim(
    *,
    evenement,
    date_fin_interim,
):
    """
    Crée la fiche spécialisée de fin
    d'intérim.

    Cette fiche prépare la clôture
    de l'occupation temporaire.

    Elle ne produit aucun effet tant
    que l'événement n'est pas validé.
    """

    return FinInterim.objects.create(

        evenement=evenement,

        date_fin_interim=date_fin_interim,
    )

# ==========================================================
# Démission
# ==========================================================

def creer_demission(
    *,
    evenement,
    motif=None,
):
    """
    Crée la fiche spécialisée
    de démission.
    """

    return Demission.objects.create(

        evenement=evenement,

        motif=motif,
    )


# ==========================================================
# Retraite
# ==========================================================

def creer_retraite(
    *,
    evenement,
    motif=None,
):
    """
    Crée la fiche spécialisée
    de retraite.
    """

    return Retraite.objects.create(

        evenement=evenement,

        motif=motif,
    )


# ==========================================================
# Radiation
# ==========================================================

def creer_radiation(
    *,
    evenement,
    motif=None,
):
    """
    Crée la fiche spécialisée
    de radiation.
    """

    return Radiation.objects.create(

        evenement=evenement,

        motif=motif,
    )

# ==========================================================
# Détachement
# ==========================================================

def creer_detachement(
    *,
    evenement,
    organisme_accueil,
    structure,
    unite,
    date_debut,
    date_fin,
):
    """
    Crée la fiche spécialisée de détachement.

    Cette fiche constitue les données
    préparatoires de l'événement.

    Elle n'a aucun effet sur la carrière
    tant que l'événement n'est pas validé.
    """

    return Detachement.objects.create(

        evenement=evenement,

        organisme_accueil=organisme_accueil,

        structure_id=structure,

        unite_id=unite,

        date_debut=date_debut,

        date_fin=date_fin,
    )

# ==========================================================
# Mise à disposition
# ==========================================================

def creer_mise_a_disposition(
    *,
    evenement,
    organisme_accueil,
    structure,
    unite,
    date_debut,
    date_fin,
):
    """
    Crée la fiche spécialisée de mise
    à disposition.

    Cette fiche constitue les données
    préparatoires de l'événement.

    Elle n'a aucun effet sur la carrière
    tant que l'événement n'est pas validé.
    """

    return MiseADisposition.objects.create(

        evenement=evenement,

        organisme_accueil=organisme_accueil,

        structure_id=structure,

        unite_id=unite,

        date_debut=date_debut,

        date_fin=date_fin,
    )

# ==========================================================
# Disponibilité
# ==========================================================

def creer_disponibilite(
    *,
    evenement,
    motif,
    date_debut,
    date_fin,
):
    """
    Crée la fiche spécialisée
    de disponibilité.

    Cette fiche constitue les données
    préparatoires de l'événement.

    Elle n'a aucun effet sur la carrière
    tant que l'événement n'est pas validé.
    """

    return Disponibilite.objects.create(

        evenement=evenement,

        motif=motif,

        date_debut=date_debut,

        date_fin=date_fin,
    )

# ==========================================================
# DÉCISION DE CONGÉ
# ==========================================================


def creer_decision_conge(
    *,
    evenement,
    type_conge,
    nombre_jours_accordes,
):
    """
    Crée une décision de congé.

    Cette décision matérialise l'acte administratif
    accordant un droit à congé à un agent.

    La consommation effective des jours sera assurée
    ultérieurement par les entités Conge.
    """

    return DecisionConge.objects.create(

        evenement=evenement,

        type_conge=type_conge,

        nombre_jours_accordes=(
            nombre_jours_accordes
        ),
    )

# ==========================================================
# COMPTEUR DE CONGÉ
# ==========================================================


def creer_compteur_conge(
    *,
    decision_conge,
):
    """
    Crée le compteur associé à une
    décision de congé.

    Une décision de congé possède
    un compteur unique.
    """

    return CompteurConge.objects.create(

        decision_conge=decision_conge,

    )

# ==========================================================
# MOUVEMENT DE COMPTEUR DE CONGÉ
# ==========================================================


def creer_mouvement_compteur_conge(
    *,
    compteur,
    type_mouvement,
    nombre_jours,
    date_mouvement,
    observation=None,
):
    """
    Crée un mouvement sur un compteur
    de congé.

    Chaque mouvement est historisé et
    représente une opération métier
    affectant le compteur.
    """

    return MouvementCompteurConge.objects.create(

        compteur=compteur,

        type_mouvement=type_mouvement,

        nombre_jours=nombre_jours,

        date_mouvement=date_mouvement,

        observation=observation,

    )