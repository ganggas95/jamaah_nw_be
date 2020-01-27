"""Serializer for Login module"""
from flask_marshmallow import Schema


class LoginSerializers(Schema):
    """Serializers object for login moodel"""

    class Meta:
        """Meta class"""
        fields = [
            'token',
            'refresh_token',
        ]
