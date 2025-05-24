from django.apps import AppConfig


class BelledemeureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'belledemeure'

    def ready(self):
        import belledemeure.signals


