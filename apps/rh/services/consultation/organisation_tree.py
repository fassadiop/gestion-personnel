from apps.rh.models.organisation import (
    Poste,
    Structure,
    UniteOrganisationnelle,
)


class OrganisationTreeService:
    """
    Service de construction de l'arborescence
    organisationnelle des structures.

    Retourne :
    - les structures ;
    - leurs postes directement rattachés ;
    - leurs unités organisationnelles hiérarchisées ;
    - les postes rattachés à chaque unité.
    """

    @classmethod
    def execute(cls):
        structures = (
            Structure.objects
            .filter(actif=True)
            .select_related(
                "type_structure",
            )
            .order_by("nom")
        )

        return {
            "structures": [
                cls._build_structure(structure)
                for structure in structures
            ]
        }

    @classmethod
    def _build_structure(cls, structure):
        """
        Construit une structure avec ses unités racines
        et ses éventuels postes directement rattachés.
        """

        unites_racines = (
            UniteOrganisationnelle.objects
            .filter(
                structure=structure,
                parent__isnull=True,
                actif=True,
            )
            .select_related(
                "type_unite",
                "responsable",
            )
            .order_by(
                "ordre",
                "nom",
            )
        )

        postes_structure = (
            Poste.objects
            .filter(
                structure=structure,
                unite__isnull=True,
                actif=True,
            )
            .select_related(
                "hierarchie_minimale",
            )
            .order_by("libelle")
        )

        return {
            "id": structure.id,
            "code": structure.code,
            "sigle": structure.sigle,
            "nom": structure.nom,
            "type_structure": {
                "code": structure.type_structure.code,
                "libelle": structure.type_structure.libelle,
            },
            "postes": [
                cls._build_poste(poste)
                for poste in postes_structure
            ],
            "unites": [
                cls._build_unite(unite)
                for unite in unites_racines
            ],
        }

    @classmethod
    def _build_unite(cls, unite):
        """
        Construit récursivement une unité organisationnelle.
        """

        enfants = (
            unite.enfants
            .filter(actif=True)
            .select_related(
                "type_unite",
                "responsable",
            )
            .order_by(
                "ordre",
                "nom",
            )
        )

        postes = (
            unite.postes
            .filter(actif=True)
            .select_related(
                "hierarchie_minimale",
            )
            .order_by("libelle")
        )

        return {
            "id": unite.id,
            "code": unite.code,
            "sigle": unite.sigle,
            "nom": unite.nom,
            "ordre": unite.ordre,
            "type_unite": {
                "code": unite.type_unite.code,
                "libelle": unite.type_unite.libelle,
            },
            "responsable": (
                str(unite.responsable)
                if unite.responsable
                else None
            ),
            "postes": [
                cls._build_poste(poste)
                for poste in postes
            ],
            "enfants": [
                cls._build_unite(enfant)
                for enfant in enfants
            ],
        }

    @classmethod
    def _build_poste(cls, poste):
        """
        Construit la représentation d'un poste.
        """

        return {
            "id": poste.id,
            "code": poste.code,
            "libelle": poste.libelle,
            "est_responsable": poste.est_responsable,
            "est_budgetise": poste.est_budgetise,
            "hierarchie_minimale": (
                str(poste.hierarchie_minimale)
                if poste.hierarchie_minimale
                else None
            ),
        }