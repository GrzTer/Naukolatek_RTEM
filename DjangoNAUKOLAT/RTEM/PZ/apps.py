from django.apps import AppConfig
from django.conf import settings
from keras.models import load_model


class PzAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "PZ"
    model = None

    def ready(self):
        self.model = load_model(settings.MODEL_PATH)
