"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/organisation/base.py

Description :
    Classe de base des serializers
    du domaine Organisation.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from apps.rh.serializers.base import BaseSerializer


class BaseOrganisationSerializer(
    BaseSerializer
):
    """
    Classe de base des serializers
    du domaine Organisation.
    """

    class Meta(BaseSerializer.Meta):
        pass