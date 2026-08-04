"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : serializers/base.py

Description :
    Classe de base de tous les serializers
    du SGCP.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    """
    Classe de base de tous les serializers
    du SGCP.

    Cette classe centralise uniquement les
    fonctionnalités réellement communes à tous
    les serializers.

    Aucune logique métier ne doit être implémentée
    ici.
    """

    # =====================================================
    # Contexte
    # =====================================================

    @property
    def request(self):
        """
        Retourne la requête HTTP courante.
        """
        return self.context.get("request")

    @property
    def user(self):
        """
        Retourne l'utilisateur connecté.
        """
        request = self.request
        return getattr(request, "user", None)

    # =====================================================
    # Validation
    # =====================================================

    def validate(self, attrs):
        """
        Validation commune.

        Les validations métier sont réalisées
        dans les serializers spécialisés.
        """
        return super().validate(attrs)

    # =====================================================
    # Sauvegarde
    # =====================================================

    def create(self, validated_data):
        """
        Création d'une instance.
        """
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Mise à jour d'une instance.
        """
        return super().update(
            instance,
            validated_data,
        )