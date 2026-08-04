from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    Configuration de l'application
    d'authentification.
    """

    default_auto_field = (
        "django.db.models.BigAutoField"
    )

    name = "apps.authentication"

    verbose_name = (
        "Authentification"
    )