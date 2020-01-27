"""Module ORM for users"""
import uuid
from bcrypt import hashpw, checkpw, gensalt
from sqlalchemy import Column, String, Boolean
from sqlalchemy import or_
from flask_sqlalchemy import Pagination
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from jamaah.factory import db
from jamaah.models.wilayah import Kabupaten, Kecamatan


class Users(db.Model):
    """Class ORM for users"""
    __tablename__ = "users"
    uid = Column(String(200), primary_key=True, autoincrement=False)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    role = Column(String(200))
    kecamatan_id = Column(String(20), default=None)
    kabupaten_id = Column(String(20), default=None)
    active = Column(Boolean, default=True)
    _password = Column("password", String(200))

    def __init__(self, username, email, password=None):
        super(Users, self).__init__()
        self.uid = str(uuid.uuid1())
        self.username = username
        self.email = email
        self.active = True
        self.password = password

    @property
    def kabupaten(self):
        kabupaten = Kabupaten.get(self.kabupaten_id)
        return kabupaten.name if kabupaten else None

    @kabupaten.setter
    def kabupaten(self, value):
        if isinstance(value, str):
            self.kabupaten_id = value
        elif isinstance(value, dict):
            self.kabupaten_id = value["id"]

    @property
    def kecamatan(self):
        kecamatan = Kecamatan.get(self.kecamatan_id)
        return kecamatan.name if kecamatan else None

    @kecamatan.setter
    def kecamatan(self, value):
        if isinstance(value, str):
            self.kecamatan_id = value
        elif isinstance(value, dict):
            self.kecamatan_id = value["id"]

    @property
    def password(self):
        """Return password as property"""
        return self._password

    @password.setter
    def password(self, value):
        self._password = hashpw(
            str(value).encode('utf-8'),
            gensalt(rounds=12)
        )

    def from_request(self, payload: dict):
        """
        Method to handle set attribute by given request payload
            :params `payload`: Request payload
        """
        except_fields = ["uid", "conf_password"]
        for key in payload:
            if not isinstance(payload[key], dict) and key not in except_fields:
                
                setattr(self, key, payload[key])

    @property
    def is_exist(self):
        """Method is exist to check user is exist"""
        return self.by_username(self.username) is not None

    @staticmethod
    def get_list_users(search: str, page: int) -> Pagination:
        """
            Query method to handle query user
                :params `search`: keyword to search user
                :params `page`: number of page used by paginate
        """
        return Users.query.filter(
            or_(
                Users.username.like(f"%{search}%"),
                Users.email.like(f"%{search}%"),
            )
        ).paginate(page=page, per_page=15)

    @staticmethod
    def by_username(username: str) -> object:
        """
            Query method to handle query user by username
                :params `username`: Username of user
        """
        return Users.query.filter(
            Users.username == username
        ).first()

    @staticmethod
    def get(user_id: str) -> object:
        """
            Query method to handle query user by user_id
                :params `user_id`: ID of user
        """
        return Users.query.get(user_id)

    def check_password(self, password: str) -> bool:
        """
            Method to handle checking password
        """
        return checkpw(
            str(password).encode('utf-8'),
            str(self.password).encode('utf-8')
        )

    @property
    def access_token(self):
        """Method to handle create token return as property"""
        return create_access_token(identity=self.username)

    @property
    def refresh_token(self):
        """Method to handle create refresh token return as property"""
        return create_refresh_token(identity=self.username)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
