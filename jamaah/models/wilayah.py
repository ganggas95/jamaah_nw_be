"""Module of data wilayah administrative"""
from sqlalchemy import (Column, String, Text, Float)
from jamaah.factory import db


class Desa(db.Model):
    """Desa Module"""
    __tablename__ = 'desa'
    id = Column(String(20), primary_key=True, autoincrement=False)
    name = Column(String(200))
    kec_id = Column(String(200))

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @property
    def is_exist(self):
        """Check data is exist or not exist"""
        return self.get(self.id) is not None

    @classmethod
    def get_by_desa(cls, kec_id):
        """Get data desa from kode desa"""
        return cls.query.filter(cls.kec_id == kec_id).all()


class Kecamatan(db.Model):
    """Kecamatan Module"""
    __tablename__ = 'kecamatan'
    id = Column(String(20), primary_key=True, autoincrement=False)
    name = Column(String(200))
    kab_id = Column(String(200))

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @property
    def is_exist(self):
        """Check data is exist or not exist"""
        return self.get(self.id) is not None

    @classmethod
    def get_by_kabupaten(cls, kab_id):
        """Get data kabupaten from kode kabupaten"""
        return cls.query.filter(cls.kab_id == kab_id).all()


class Kabupaten(db.Model):
    """Kabupaten Module"""
    __tablename__ = 'kabupaten'
    id = Column(String(20), primary_key=True, autoincrement=False)
    name = Column(String(200))
    prov_id = Column(String(200))

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @property
    def is_exist(self):
        """Check data object in database exist"""
        return self.get(self.id) is not None

    @classmethod
    def get_by_provinsi(cls, prov_id):
        """Get data provinsi from kode provinsi"""
        return cls.query.filter(cls.prov_id == prov_id).all()


class Provinsi(db.Model):
    """Provinsi Module"""
    __tablename__ = 'provinsi'
    id = Column(String(20), primary_key=True, autoincrement=False)
    name = Column(String(200))

    def __init__(self, kode_prov, name):
        super(Provinsi, self).__init__()
        self.id = kode_prov
        self.name = name
    
    @staticmethod
    def get_all():
        return Provinsi.query.all()

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @property
    def is_exist(self):
        """Check object is exist"""
        return self.get(self.id) is not None
