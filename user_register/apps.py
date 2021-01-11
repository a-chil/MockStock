from django.apps import AppConfig


class UserRegisterConfig(AppConfig):
    name = "user_register"

    def ready(self):
        import user_register.signals
