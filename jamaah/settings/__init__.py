from .local import Local
from .production import Production
from .testing import Testing


app_config = {
    "local": Local,
    "production": Production,
    "testing": Testing
}
