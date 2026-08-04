# apps/rh/services/evenements/handlers/__init__.py

"""
Chargement des handlers du moteur de carrière.
"""

"""
Chargement des handlers du moteur de carrière.
"""

from .recrutement import RecrutementHandler
from .prise_service_initiale import PriseServiceInitialeHandler
from .affectation import AffectationHandler
from .prise_service_affectation import PriseServiceAffectationHandler
from .nomination import NominationHandler
from .titularisation import TitularisationHandler
from .reclassement import ReclassementHandler
from .mutation import MutationHandler
from .mise_a_disposition import MiseADispositionHandler
from .detachement import DetachementHandler
from .reintegration import ReintegrationHandler
from .disponibilite import DisponibiliteHandler
from .interim import InterimHandler
from .fin_interim import FinInterimHandler
from .demission import DemissionHandler
from .radiation import RadiationHandler
from .retraite import RetraiteHandler
from .decision_conge import DecisionCongeHandler
from .conge import CongeHandler
from .absence import AbsenceHandler
from .conge_maladie import CongeMaladieHandler
from .conge_maternite import CongeMaterniteHandler
from .inaptitude_medicale import InaptitudeMedicaleHandler
from .restriction_medicale import RestrictionMedicaleHandler
from .accident_travail import AccidentTravailHandler
from .reprise_service import RepriseServiceHandler