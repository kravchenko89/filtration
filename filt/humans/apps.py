from django.apps import AppConfig


class HumansConfig(AppConfig):
    name = 'humans'

    def ready(self):
        import humans.signals
