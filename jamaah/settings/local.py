from jamaah.settings.base import BaseSetting


class Local(BaseSetting):
    ENV = "development"
    DEBUG = True
