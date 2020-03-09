from django.apps import AppConfig


class RecappConfig(AppConfig):
    name = 'RecApp'
    def ready():
        return import Recommender