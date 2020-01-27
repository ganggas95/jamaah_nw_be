"""All provider will be listed here"""
from jamaah.provider.login_provider import LoginProvider
from jamaah.provider.wilayah_provider import WilayahProvider
from jamaah.provider.jamaah_provider import JamaahProvider


PROVIDERS = [
    LoginProvider,
    # UserProvider,
    WilayahProvider,
    JamaahProvider,
]
