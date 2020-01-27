import os
from datetime import timedelta
from kombu import Queue
from kombu import Exchange


class BaseSetting:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    API_VERSION = os.getenv("API_VERSION", "v0.1")
    API_ROOT = f"/api/{API_VERSION}"
    JWT_TOKEN_LOCATION = "headers"
    JWT_CSRF_IN_COOKIES = False
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_ACCESS_COOKIE_PATH = "{}{}".format(API_ROOT, "/login")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)
    CORS_HEADERS = 'Content-Type, Authorization, Accept'
    ORIGINS = "*"
    ALLOWED_EXTENSION = set(["png", "jpeg", "jpg", "pdf", "zip", "rar"])
    FILE_IMPORT_FOLDER = os.path.join("data_import")
    UPLOAD_DIR_DATA = os.path.join("uploads")
    EXPORT_DIR_DATA = os.path.join("data_export")

    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", None)
    CLEERY_BACKEND = CELERY_BROKER_URL
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", None)
    CELERY_DEFAULT_QUEUE = 'default'

    CELERY_IMPORTS = (
        "jamaah.tasks",
    )
    # CELERY_TASK_RESULT_EXPIRES = 30
    CELERY_TIMEZONE = 'UTC'
    USE_TZ = True
    CELERY_ENABLE_UTC = False
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_RESULT_EXPIRES = 120  # 2 mins
    CELERYD_CONCURRENCY = 6
    CELERYD_MAX_TASKS_PER_CHILD = 4
    CELERYD_PREFETCH_MULTIPLIER = 1
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
    CELERY_DEFAULT_QUEUE = 'jamaah_tasks'

    CELERY_QUEUES = (
        Queue('default', Exchange('default'), routing_key='default'),
        Queue('jamaah_tasks', Exchange('jamaah_tasks'), routing_key='jamaah_tasks_tasks'),
    )
