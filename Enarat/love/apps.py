from django.apps import AppConfig


class LoveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'love'

    def ready(self):
        import love.signals