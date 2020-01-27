from flask import Request
from flask_jwt_extended import get_jwt_identity
from jamaah.provider.base import Provider
from jamaah.serializers.login_serializers import LoginSerializers
from jamaah.models.users import Users


class LoginProvider(Provider):
    login_serializer = LoginSerializers()
    error_login = {"username": "Username is invalid", "password": "Password is invalid"}
    error_refresh = {"refresh_token": "Invalid refresh token"}

    @staticmethod
    def get_by_username(username: str) -> Users:
        return Users.by_username(username)

    @property
    def current_user(self) -> Users:
        return self.get_by_username(get_jwt_identity())

    def login_user(self, payload: Request) -> tuple:
        payload = payload.get_json(force=True)
        username = payload.get("username", None)
        password = payload.get("password", None)
        results = None
        if username and password:
            user = self.get_by_username(username)
            results = {
                "access_token": user.access_token,
                "refresh_token": user.refresh_token,
            } if user and user.check_password(password) else None
        return results, None if results is not None else self.error_login

    def refresh_token(self) -> dict:
        return {
            "access_token": self.current_user.access_token,
            "refresh_token": self.current_user.refresh_token,
        } if self.current_user else None
