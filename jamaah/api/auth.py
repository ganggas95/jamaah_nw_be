"""Module API for Authentication"""
from flask.views import View
from flask import request
from injector import inject
from jamaah.provider.login_provider import LoginProvider


class AuthAPI(View):
    """Class Auth API"""
    login_provider = LoginProvider()

    def dispatch_request(self):
        """Handle request to login"""
        login_result, errors = self.login_provider.login_user(request)
        status = 200 if login_result else 403
        msg = "Login successfully" if login_result else "Login failed"
        return self.login_provider.create_response(
            status=status,
            data=login_result,
            msg=msg,
            errors=errors
        )
