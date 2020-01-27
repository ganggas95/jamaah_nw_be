from flask_injector import Binder
from jamaah.provider import PROVIDERS


def configure(binder: Binder):
    for provider in PROVIDERS:
        binder.bind(provider, to=provider)
