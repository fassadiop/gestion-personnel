import hashlib
import mimetypes
from pathlib import Path


class DocumentMetadataService:
    """
    Service chargé d'extraire les métadonnées techniques
    d'un fichier documentaire.

    Ce service ne contient aucune règle métier liée
    aux documents administratifs ou aux documents agents.
    """

    @staticmethod
    def extraire(fichier):
        """
        Extrait les métadonnées techniques du fichier.

        Retourne :
        - nom_fichier
        - extension
        - taille
        - mime_type
        - hash_document
        """

        if not fichier:
            return {}

        nom_original = Path(fichier.name)

        extension = nom_original.suffix.lower()

        # Le nom du fichier est conservé sans l'extension,
        # conformément à BaseDocument.nom_complet.
        nom_fichier = nom_original.stem

        taille = fichier.size

        mime_type = (
            getattr(fichier, "content_type", None)
            or mimetypes.guess_type(fichier.name)[0]
            or "application/octet-stream"
        )

        sha256 = hashlib.sha256()

        # On repart du début du fichier avant lecture.
        fichier.seek(0)

        for chunk in fichier.chunks():
            sha256.update(chunk)

        # Important : repositionner le curseur afin que
        # Django puisse ensuite enregistrer le fichier.
        fichier.seek(0)

        return {
            "nom_fichier": nom_fichier,
            "extension": extension,
            "taille": taille,
            "mime_type": mime_type,
            "hash_document": sha256.hexdigest(),
        }