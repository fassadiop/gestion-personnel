from django.apps import AppConfig


class RhConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.rh"
    verbose_name = "Ressources Humaines"

    def ready(self):
        """
        Initialise les registres métier.

        Les imports sont réalisés uniquement
        au démarrage de l'application afin
        d'enregistrer automatiquement tous
        les Handlers et tous les Creators.
        """

        # Moteur de carrière
        import apps.rh.services.evenements.handlers

        # Moteur de création
        import apps.rh.services.creation.creators