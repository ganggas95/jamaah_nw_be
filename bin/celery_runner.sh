#!/bin/bash
export PYTHONPATH=$FLASKDIR:$PYTHONPATH
export PYTHONUNBUFFERED=1
export ENV=local
export HOST=0.0.0.0
export PORT=2020
export FLASK_APP=app
export FLASK_DEBUG=1
export DATABASE_URI=mysql+pymysql://root:b1sm1llah@localhost:33061/jamaah_app_db
export API_VERSION=v0.1
export SECRET_KEY=YjFzbTFsbGFoMTI5MDMyMyoqKiYmJkBeIypAKioyNAo
export CELERY_BROKER_URL=redis://localhost:6379/5
export CELERY_RESULT_BACKEND=redis://localhost:6379/6

python celery_runner.py worker  -l info -Q jamaah_tasks -B
