"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : apps/administration/models/profil_administration.py
Description :
    Modèles du domaine Administration.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from apps.rh.core.base import BaseModel
from apps.rh.models.organisation import Structure


class ProfilAdministration(BaseModel):
    """
    Informations d'administration associées
    à un utilisateur Django.

    Ce modèle complète django.contrib.auth.User
    avec les informations propres au SGCP.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profil_administration",
        verbose_name="Utilisateur",
    )

    structure_racine = models.ForeignKey(
        Structure,
        on_delete=models.PROTECT,
        related_name="administrateurs",
        limit_choices_to={
            "parent__isnull": True,
        },
        null=True,
        blank=True,
        verbose_name="Structure racine",
        help_text=(
            "Structure Racine administrée par "
            "cet utilisateur."
        ),
    )

    class Meta:
        db_table = "adm_profil_administration"
        verbose_name = (
            "Profil d'administration"
        )
        verbose_name_plural = (
            "Profils d'administration"
        )

    def clean(self):
        """
        Le SuperUser peut ne pas être
        rattaché à une Structure Racine.

        Tous les autres utilisateurs doivent
        obligatoirement administrer une
        Structure Racine.
        """

        if (
            not self.user.is_superuser
            and self.structure_racine is None
        ):
            raise ValidationError(
                {
                    "structure_racine": (
                        "La Structure Racine est "
                        "obligatoire pour tout "
                        "utilisateur non SuperUser."
                    )
                }
            )

    def __str__(self):
        if self.user.is_superuser:
            return (
                f"{self.user.username} "
                "(SuperUser)"
            )

        return (
            f"{self.user.get_full_name()} - "
            f"{self.structure_racine}"
        )