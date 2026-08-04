"""
Groupes d'événements utilisés par les services métier.

Ces constantes servent notamment à :
- filtrer les documents administratifs ;
- construire les tableaux de bord ;
- effectuer les recherches multicritères ;
- alimenter les statistiques RH.

Toute modification de ces groupes doit être réalisée ici.
"""

# ==========================================================
# ÉVÉNEMENTS MÉDICAUX
# ==========================================================

EVENEMENTS_MEDICAUX = (
    "CONGE_MALADIE",
    "CONGE_MATERNITE",
    "ACCIDENT_TRAVAIL",
    "INAPTITUDE_MEDICALE",
    "RESTRICTION_MEDICALE",
)