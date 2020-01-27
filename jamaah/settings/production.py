from jamaah.settings.base import BaseSetting


class Production(BaseSetting):
    ENV = "production"
    DEBUG = False
