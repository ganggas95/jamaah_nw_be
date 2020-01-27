import os
from jamaah.factory import app, jwt, celery_flask
from jamaah.models.users import Users
from jamaah.serializers.user_serializers import UserSerializers
from jamaah.urls import login_url
from jamaah.urls import wilayah_url
from jamaah.urls import jamaah_url
from jamaah.urls import user_url
from jamaah.urls import tasks_url
from jamaah.urls import file_url
from jamaah.tasks.jamaah_tasks import JamaahTasks

app = login_url(app)
app = wilayah_url(app)
app = jamaah_url(app)
app = user_url(app)
app = tasks_url(app)
app = file_url(app)


def register_task():
    celery_flask.tasks.register(JamaahTasks())


register_task()


@jwt.user_loader_callback_loader
def get_user(username):
    """Method to handle get user and set user to current user"""
    return Users.by_username(username)


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    """Set current user to token claims payload"""
    user = Users.by_username(identity)
    return UserSerializers().dump(user)


@app.cli.command("create-user")
def create_user():
    username = "admin"
    email = "admin@li.com"
    password = "admin212"
    user = Users.by_username(username)
    if user is None:
        user = Users(username, email, password)
    else:
        user.password = password
    user.save()
    print("Finish")
