from django.apps import AppConfig


class MtaaConfig(AppConfig):
    name = 'mtaa'

    def ready(self):
        import mtaa.signals
