from django.apps import AppConfig


class authenticateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticate'

    def ready(self) :
        import authenticate.signals