from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from CeleryFlask import CeleryFlask

db = SQLAlchemy()
ma = Marshmallow()
celery_flask = CeleryFlask()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()
