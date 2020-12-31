from django.apps import AppConfig


class CarsConfig(AppConfig):
    name = 'cars'

    def ready(self):
        print("===================Cars App=====================")
        import cars.signals