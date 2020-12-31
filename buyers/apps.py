from django.apps import AppConfig


class BuyersConfig(AppConfig):
    name = 'buyers'

    def ready(self):
        print("=============================Inside ready=============================")
        import buyers.signals
