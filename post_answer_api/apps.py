from django.apps import AppConfig


class PostAnswerApiConfig(AppConfig):
    name = 'post_answer_api'

    def ready(self):
        import post_answer_api.signals
