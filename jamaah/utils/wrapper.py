from functools import wraps
from flask_jwt_extended import current_user as user
from jamaah.utils.response import create_response


def requires_groups(*groups):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if user is None:
                return create_response(403, msg="Forbidden access")
            if user.role not in groups:
                return create_response(403, msg="Access not allowed")
            return f(*args, **kwargs)
        return wrapped
    return wrapper
