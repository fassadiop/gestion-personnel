# apps/administration/urls.py

from rest_framework.routers import DefaultRouter

from apps.administration.views.groupe import GroupeViewSet
from apps.administration.views.permission import PermissionViewSet
from apps.administration.views.profil_administration import ProfilAdministrationViewSet
from apps.administration.views.utilisateur import (
    UtilisateurViewSet,
)

router = DefaultRouter()

router.register(
    r"utilisateurs",
    UtilisateurViewSet,
    basename="utilisateur",
)

router.register(
    r"groupes",
    GroupeViewSet,
    basename="groupe",
)

router.register(
    r"permissions",
    PermissionViewSet,
    basename="permission",
)

router.register(
    r"profils",
    ProfilAdministrationViewSet,
    basename="profil-administration",
)

urlpatterns = router.urls