from django.apps import AppConfig


class LikesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Likes'
    def ready(self) -> None:
        import Likes.signals
