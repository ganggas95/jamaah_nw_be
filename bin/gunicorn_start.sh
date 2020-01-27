#!/bin/bash

NAME="jamaah_be"                                  # Name of the application
FLASKDIR=/home/almuma/$NAME             # Django project directory
SOCKFILE=/home/almuma/$NAME/run/gunicorn.sock  # we will communicte using this unix socket
USER=almuma                                       # the user to run a
GROUP=almuma                        # the group to run as
NUM_WORKERS=2                                     # how many worker processes should Gunicorn spawn
#DJANGO_SETTINGS_MODULE=hello.settings             # which settings file should Django use
#DJANGO_WSGI_MODULE=hello.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $FLASKDIR
source ./venv/bin/activate
#export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$FLASKDIR:$PYTHONPATH
export PYTHONUNBUFFERED=1
export ENV=local
export HOST=0.0.0.0
export PORT=2020
export FLASK_APP=app
export FLASK_DEBUG=1
export DATABASE_URI=mysql+pymysql://root:b1sm1llah@localhost/jamaah_app_db
export API_VERSION=v0.1
export SECRET_KEY=YjFzbTFsbGFoMTI5MDMyMyoqKiYmJkBeIypAKioyNAo
export CELERY_BROKER_URL=redis://localhost:6379/5
export CELERY_RESULT_BACKEND=redis://localhost:6379/5
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ./venv/bin/gunicorn app:app_instance \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
