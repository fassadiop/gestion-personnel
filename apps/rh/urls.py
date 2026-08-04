"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : apps/rh/urls.py

Description :
    Routes de l'API RH.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.urls import include
from django.urls import path

from apps.rh.views.accident_travail.accident_travail import AccidentTravailViewSet
from apps.rh.views.conge_maladie.conge_maladie import CongeMaladieViewSet
from apps.rh.views.conge_maternite.conge_maternite import CongeMaterniteViewSet
from apps.rh.views.consultation.cv_carriere import CVCarriereView
from apps.rh.views.consultation.timeline import TimelineView
from apps.rh.views.consultation.statistiques import (
    StatistiquesView,
)
from apps.rh.views.consultation.organisation import (
    OrganisationTreeView,
)
from apps.rh.views.consultation.conges_agent import (
    CongesAgentView,
)
from apps.rh.views.consultation.absences_agent import (
    AbsencesAgentView,
)
from apps.rh.views.consultation.documents_agent import (
    DocumentsAgentView,
)

from apps.rh.views.conges.compteur_conge import CompteurCongeViewSet
from apps.rh.views.conges.mouvement_compteur_conge import MouvementCompteurCongeViewSet
from apps.rh.views.consultation.dashboard import DashboardView
from apps.rh.views.dossier_medical.dossier_medical import DossierMedicalView
from apps.rh.views.fin_interim.fin_interim import FinInterimViewSet
from apps.rh.views.inaptitude_medicale.inaptitude_medicale import InaptitudeMedicaleViewSet
from apps.rh.views.interim.interim import InterimViewSet
from apps.rh.views.mise_a_disposition.mise_a_disposition import MiseADispositionViewSet
from apps.rh.views.radiation.radiation import RadiationViewSet
from apps.rh.views.referentiels.evenement.statut_evenement import StatutEvenementViewSet
from rest_framework.routers import DefaultRouter

from apps.rh.views.prise_service_affectation.prise_service_affectation import PriseServiceAffectationViewSet
from apps.rh.views.prise_service_initiale.prise_service_initiale import PriseServiceInitialeViewSet
from apps.rh.views.referentiels.agent import EtatCivilViewSet, NationaliteViewSet, SexeViewSet, StatutAgentViewSet
from apps.rh.views.referentiels.rh.type_inaptitude_medicale import TypeInaptitudeMedicaleViewSet
from apps.rh.views.referentiels.rh.type_mouvement_conge import TypeMouvementCongeViewSet
from apps.rh.views.referentiels.statut.corps import (
    CorpsViewSet,
)
from apps.rh.views.referentiels.statut.grade import (
    GradeViewSet,
)
from apps.rh.views.referentiels.statut.classe import (
    ClasseViewSet,
)
from apps.rh.views.referentiels.statut.echelon import (
    EchelonViewSet,
)
from apps.rh.views.referentiels.statut.position_administrative import (
    PositionAdministrativeViewSet,
)
from apps.rh.views.referentiels.statut.hierarchie import (
    HierarchieViewSet,
)
from apps.rh.views.referentiels.rh.type_absence import (
    TypeAbsenceViewSet,
)
from apps.rh.views.referentiels.rh.type_competence import (
    TypeCompetenceViewSet,
)
from apps.rh.views.referentiels.rh.type_conge import (
    TypeCongeViewSet,
)
from apps.rh.views.referentiels.rh.type_decoration import (
    TypeDecorationViewSet,
)
from apps.rh.views.referentiels.rh.type_formation import (
    TypeFormationViewSet,
)
from apps.rh.views.referentiels.rh.type_sanction import (
    TypeSanctionViewSet,
)
from apps.rh.views.referentiels.geographie.pays import (
    PaysViewSet,
)
from apps.rh.views.referentiels.formation.organisme_formation import (
    OrganismeFormationViewSet,
)
from apps.rh.views.referentiels.formation.source_financement import (
    SourceFinancementViewSet,
)
from apps.rh.views.referentiels.document.type_document import (
    TypeDocumentViewSet,
)
from apps.rh.views.referentiels.document.type_document_medical import (
    TypeDocumentMedicalViewSet,
)
from apps.rh.views.referentiels.evenement.type_evenement import (
    TypeEvenementViewSet,
)
from apps.rh.views.organisation.type_structure import (
    TypeStructureViewSet,
)
from apps.rh.views.organisation.structure import (
    StructureViewSet,
)
from apps.rh.views.organisation.type_unite_organisationnelle import (
    TypeUniteOrganisationnelleViewSet,
)
from apps.rh.views.organisation.unite_organisationnelle import (
    UniteOrganisationnelleViewSet,
)
from apps.rh.views.organisation.poste import (
    PosteViewSet,
)
from apps.rh.views.documents.document_administratif import (
    DocumentAdministratifViewSet,
)
from apps.rh.views.documents.document_agent import (
    DocumentAgentViewSet,
)
from apps.rh.views.carriere.situation_administrative import (
    SituationAdministrativeViewSet,
)
from apps.rh.views.affectation.affectation import (
    AffectationViewSet,
)
from apps.rh.views.occupation.occupation_poste import (
    OccupationPosteViewSet,
)
from apps.rh.views.recrutement.recrutement import (
    RecrutementViewSet,
)
from apps.rh.views.reclassement.reclassement import (
    ReclassementViewSet,
)
from apps.rh.views.reprise_service.reprise_service import RepriseServiceViewSet
from apps.rh.views.restriction_medicale.restriction_medicale import RestrictionMedicaleViewSet
from apps.rh.views.titularisation.titularisation import (
    TitularisationViewSet,
)
from apps.rh.views.nomination.nomination import (
    NominationViewSet,
)
from apps.rh.views.mutation.mutation import (
    MutationViewSet,
)
from apps.rh.views.demission.demission import (
    DemissionViewSet,
)
from apps.rh.views.detachement.detachement import (
    DetachementViewSet,
)
from apps.rh.views.disponibilite.disponibilite import (
    DisponibiliteViewSet,
)
from apps.rh.views.reintegration.reintegration import (
    ReintegrationViewSet,
)
from apps.rh.views.retraite.retraite import (
    RetraiteViewSet,
)
from apps.rh.views.evaluation.evaluation import (
    EvaluationViewSet,
)
from apps.rh.views.formation.formation import (
    FormationViewSet,
)
from apps.rh.views.competence.niveau_competence import (
    NiveauCompetenceViewSet,
)
from apps.rh.views.agent.agent import (
    AgentViewSet,
)
from apps.rh.views.evenement.evenement import (
    EvenementCarriereViewSet,
)
from apps.rh.views.conges.decision_conge import (
    DecisionCongeViewSet,
)
from apps.rh.views.conges.conge import (
    CongeViewSet,
)
from apps.rh.views.absence.absence import (
    AbsenceViewSet,
)
from apps.rh.views.missions.mission import (
    MissionViewSet,
)
from apps.rh.views.decoration.decoration import (
    DecorationViewSet,
)
from apps.rh.views.sanction.sanction import (
    SanctionViewSet,
)
from apps.rh.views.medical.dossier_medical import (
    DossierMedicalViewSet,
)
from apps.rh.views.medical.document_medical import (
    DocumentMedicalViewSet,
)


router = DefaultRouter()

# ==========================================================
# Référentiels - Statut
# ==========================================================

router.register(
    r"referentiels/corps",
    CorpsViewSet,
    basename="corps",
)

router.register(
    r"referentiels/grades",
    GradeViewSet,
    basename="grade",
)

router.register(
    r"referentiels/classes",
    ClasseViewSet,
    basename="classe",
)

router.register(
    r"referentiels/echelons",
    EchelonViewSet,
    basename="echelon",
)

router.register(
    r"referentiels/positions-administratives",
    PositionAdministrativeViewSet,
    basename="position-administrative",
)

# ==========================================================
# Référentiels - RH
# ==========================================================

router.register(
    r"referentiels/types-absences",
    TypeAbsenceViewSet,
    basename="type-absence",
)

router.register(
    r"referentiels/types-competences",
    TypeCompetenceViewSet,
    basename="type-competence",
)

router.register(
    r"referentiels/types-mouvements-conges",
    TypeMouvementCongeViewSet,
    basename="type-mouvement-conge",
)

router.register(
    r"referentiels/types-conges",
    TypeCongeViewSet,
    basename="type-conge",
)

router.register(
    r"referentiels/types-inaptitudes-medicales",
    TypeInaptitudeMedicaleViewSet,
    basename="type-inaptitude-medicale",
)

router.register(
    r"referentiels/types-decorations",
    TypeDecorationViewSet,
    basename="type-decoration",
)

router.register(
    r"referentiels/types-formations",
    TypeFormationViewSet,
    basename="type-formation",
)

router.register(
    r"referentiels/types-sanctions",
    TypeSanctionViewSet,
    basename="type-sanction",
)


# ==========================================================
# Référentiels - Géographie
# ==========================================================

router.register(
    r"referentiels/pays",
    PaysViewSet,
    basename="pays",
)


# ==========================================================
# Référentiels - Formation
# ==========================================================

router.register(
    r"referentiels/organismes-formations",
    OrganismeFormationViewSet,
    basename="organisme-formation",
)

router.register(
    r"referentiels/sources-financements",
    SourceFinancementViewSet,
    basename="source-financement",
)


# ==========================================================
# Référentiels - Documents
# ==========================================================

router.register(
    r"referentiels/types-documents",
    TypeDocumentViewSet,
    basename="type-document",
)

router.register(
    r"referentiels/types-documents-medicaux",
    TypeDocumentMedicalViewSet,
    basename="type-document-medical",
)


# ==========================================================
# Référentiels - Événements
# ==========================================================

router.register(
    r"referentiels/types-evenements",
    TypeEvenementViewSet,
    basename="type-evenement",
)


# ==========================================================
# Organisation
# ==========================================================

router.register(
    r"organisation/types-structures",
    TypeStructureViewSet,
    basename="type-structure",
)

router.register(
    r"organisation/structures",
    StructureViewSet,
    basename="structure",
)

router.register(
    r"organisation/types-unites-organisationnelles",
    TypeUniteOrganisationnelleViewSet,
    basename="type-unite-organisationnelle",
)

router.register(
    r"organisation/unites-organisationnelles",
    UniteOrganisationnelleViewSet,
    basename="unite-organisationnelle",
)

router.register(
    r"organisation/postes",
    PosteViewSet,
    basename="poste",
)


# ==========================================================
# Agent
# ==========================================================

router.register(
    r"agents",
    AgentViewSet,
    basename="agent",
)


# ==========================================================
# Documents
# ==========================================================

router.register(
    r"documents/administratifs",
    DocumentAdministratifViewSet,
    basename="document-administratif",
)

router.register(
    r"documents/agents",
    DocumentAgentViewSet,
    basename="document-agent",
)


# ==========================================================
# Événements de carrière
# ==========================================================

router.register(
    r"carriere/evenements",
    EvenementCarriereViewSet,
    basename="evenement-carriere",
)


# ==========================================================
# Carrière
# ==========================================================

router.register(
    r"carriere/situations-administratives",
    SituationAdministrativeViewSet,
    basename="situation-administrative",
)

router.register(
    r"carriere/affectations",
    AffectationViewSet,
    basename="affectation",
)

router.register(
    r"carriere/occupations-postes",
    OccupationPosteViewSet,
    basename="occupation-poste",
)

router.register(
    r"carriere/recrutements",
    RecrutementViewSet,
    basename="recrutement",
)

router.register(
    r"carriere/reclassements",
    ReclassementViewSet,
    basename="reclassement",
)

router.register(
    r"carriere/titularisations",
    TitularisationViewSet,
    basename="titularisation",
)

router.register(
    r"carriere/nominations",
    NominationViewSet,
    basename="nomination",
)

router.register(
    r"carriere/mutations",
    MutationViewSet,
    basename="mutation",
)

router.register(
    r"carriere/demissions",
    DemissionViewSet,
    basename="demission",
)

router.register(
    r"carriere/detachements",
    DetachementViewSet,
    basename="detachement",
)

router.register(
    r"carriere/disponibilites",
    DisponibiliteViewSet,
    basename="disponibilite",
)

router.register(
    r"carriere/reintegrations",
    ReintegrationViewSet,
    basename="reintegration",
)

router.register(
    r"carriere/retraites",
    RetraiteViewSet,
    basename="retraite",
)


# ==========================================================
# Évaluation
# ==========================================================

router.register(
    r"evaluations",
    EvaluationViewSet,
    basename="evaluation",
)


# ==========================================================
# Formation
# ==========================================================

router.register(
    r"formations",
    FormationViewSet,
    basename="formation",
)


# ==========================================================
# Compétences
# ==========================================================

router.register(
    r"competences",
    NiveauCompetenceViewSet,
    basename="niveau-competence",
)

# ==========================================================
# Congés
# ==========================================================

router.register(
    r"conges/decisions",
    DecisionCongeViewSet,
    basename="decision-conge",
)

router.register(
    r"conges/compteurs-conge",
    CompteurCongeViewSet,
    basename="compteur-conge",
)

router.register(
    r"conges/mouvements",
    MouvementCompteurCongeViewSet,
    basename="mouvement-compteur-conge",
)

router.register(
    r"conges",
    CongeViewSet,
    basename="conge",
)


# ==========================================================
# Absences
# ==========================================================

router.register(
    r"absences",
    AbsenceViewSet,
    basename="absence",
)


# ==========================================================
# Missions
# ==========================================================

router.register(
    r"missions",
    MissionViewSet,
    basename="mission",
)


# ==========================================================
# Décorations
# ==========================================================

router.register(
    r"decorations",
    DecorationViewSet,
    basename="decoration",
)


# ==========================================================
# Sanctions
# ==========================================================

router.register(
    r"sanctions",
    SanctionViewSet,
    basename="sanction",
)


# ==========================================================
# Médical
# ==========================================================

router.register(
    r"medical/dossiers",
    DossierMedicalViewSet,
    basename="dossier-medical",
)

router.register(
    r"medical/documents",
    DocumentMedicalViewSet,
    basename="document-medical",
)

router.register(
    r"referentiels/hierarchies",
    HierarchieViewSet,
    basename="hierarchie",
)

router.register(
    r"referentiels/sexes",
    SexeViewSet,
    basename="sexe",
)

router.register(
    r"referentiels/etats-civils",
    EtatCivilViewSet,
    basename="etat-civil",
)

router.register(
    r"referentiels/nationalites",
    NationaliteViewSet,
    basename="nationalite",
)

router.register(
    r"referentiels/statuts-agents",
    StatutAgentViewSet,
    basename="statut-agent",
)

router.register(
    r"prise-service-initiales",
    PriseServiceInitialeViewSet,
    basename="prise-service-initiale",
)

router.register(
    r"prise-service-affectations",
    PriseServiceAffectationViewSet,
    basename="prise-service-affectation",
)

router.register(
    r"mises-a-disposition",
    MiseADispositionViewSet,
    basename="mise-a-disposition",
)

router.register(
    r"interims",
    InterimViewSet,
    basename="interim",
)

router.register(
    r"fins-interim",
    FinInterimViewSet,
    basename="fin-interim",
)

router.register(
    r"radiations",
    RadiationViewSet,
    basename="radiation",
)

router.register(
    r"referentiels/statuts-evenements",
    StatutEvenementViewSet,
    basename="statut-evenement",
)

router.register(
    r"conges-maladie",
    CongeMaladieViewSet,
    basename="conge-maladie",
),

router.register(
    r"conges-maternite",
    CongeMaterniteViewSet,
    basename="conge-maternite",
),

router.register(
    r"inaptitudes-medicales",
    InaptitudeMedicaleViewSet,
    basename="inaptitude-medicale",
),

router.register(
    r"restrictions-medicales",
    RestrictionMedicaleViewSet,
    basename="restriction-medicale",
),

router.register(
    r"reprises-service",
    RepriseServiceViewSet,
    basename="reprise-service",
),

router.register(
    r"accidents-travail",
    AccidentTravailViewSet,
    basename="accident-travail",
),

urlpatterns = [
    path(
        "",
        include(router.urls),
    ),

    path(
        "dashboard/",
        DashboardView.as_view(),
        name="dashboard",
    ),

    path(
        "cv-carriere/<int:agent_id>/",
        CVCarriereView.as_view(),
        name="cv-carriere",
    ),

    path(
        "conges-agent/<int:agent_id>/",
        CongesAgentView.as_view(),
        name="conges-agent",
    ),

    path(
        "absences-agent/<int:agent_id>/",
        AbsencesAgentView.as_view(),
        name="absences-agent",
    ),

    path(
        "documents-agent/<int:agent_id>/",
        DocumentsAgentView.as_view(),
        name="documents-agent",
    ),

    path(
        "timeline/<int:agent_id>/",
        TimelineView.as_view(),
        name="timeline",
    ),

    path(
    "agents/<int:agent_id>/dossier-medical/",
        DossierMedicalView.as_view(),
        name="dossier-medical",
    ),

    path(
        "statistiques/",
        StatistiquesView.as_view(),
        name="statistiques",
    ),

    path(
        "organisation/",
        OrganisationTreeView.as_view(),
        name="organisation-tree",
    )
]