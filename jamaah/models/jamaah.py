from datetime import date
from sqlalchemy import (Column, String, Integer,
                        Text, ForeignKey, Boolean, DateTime)
from sqlalchemy import or_
from sqlalchemy.orm import relationship
from jamaah.models.base import BaseORM
from jamaah.factory import db
from jamaah.models.wilayah import (
    Provinsi,
    Kabupaten,
    Kecamatan,
    Desa
)


class Jamaah(db.Model, BaseORM):
    __tablename__ = 'jamaah'
    id = Column(Integer, primary_key=True)
    nama = Column(String(200))
    nik = Column(String(50), unique=True)
    jenis_kelamin = Column(String(20))
    tempat_lahir = Column(String(200))
    _tanggal_lahir = Column("tanggal_lahir", DateTime)
    alamat = Column(Text)
    provinsi_id = Column(String(5), ForeignKey('provinsi.id'))
    # provinsi = relationship("Provinsi", foreign_keys=[provinsi_id])
    kabupaten_id = Column(String(15), ForeignKey('kabupaten.id'))
    # kabupaten = relationship("Kabupaten", foreign_keys=[kabupaten_id])
    kecamatan_id = Column(String(15), ForeignKey('kecamatan.id'))
    # kecamatan = relationship("Kecamatan", foreign_keys=[kecamatan_id])
    desa_id = Column(String(15), ForeignKey('desa.id'))
    # desa = relationship("Desa", foreign_keys=[desa_id])
    dusun = Column(String(200))
    aktif = Column(Boolean, default=True)

    def __init__(self, nama, nik):
        super(Jamaah, self).__init__()
        self.nama = nama
        self.nik = nik

    def from_request(self, payload):
        self._from_request(payload, ["id", "no_induk"])

    @staticmethod
    def get(jamaah_id):
        return Jamaah.query.get(jamaah_id)

    @property
    def no_induk(self):
        return f"{self.kabupaten_id}-{self.id}"

    @property
    def tanggal_lahir(self):
        return self._tanggal_lahir.strftime("%Y-%m-%d") if self._tanggal_lahir else None

    @tanggal_lahir.setter
    def tanggal_lahir(self, value):
        self._tanggal_lahir = value

    @staticmethod
    def get_all(search='', page=1):
        return Jamaah.query.filter(
            or_(
                Jamaah.nama.like("%{}%".format(search)),
                Jamaah.nik.like("%{}%".format(search)),
            )
        ).paginate(page=page, per_page=10)

    @staticmethod
    def get_by_provinsi(provinsi_id, search='', page=1):
        return Jamaah.query.filter(
            Jamaah.provinsi_id == provinsi_id,
            or_(
                Jamaah.nama.like(f"%{search}%"),
                Jamaah.nik.like(f"%{search}%"),
            )
        ).paginate(page=page, per_page=10)

    @staticmethod
    def get_by_kabupaten(kabupaten_id, search='', page=1):
        return Jamaah.query.filter(
            Jamaah.kabupaten_id == kabupaten_id,
            or_(
                Jamaah.nama.like(f"%{search}%"),
                Jamaah.nik.like(f"%{search}%"),
            )
        ).paginate(page=page, per_page=10)

    @staticmethod
    def get_by_kecamatan(kecamatan_id, search='', page=1):
        return Jamaah.query.filter(
            Jamaah.kecamatan_id == kecamatan_id,
            or_(
                Jamaah.nama.like(f"%{search}%"),
                Jamaah.nik.like(f"%{search}%"),
            )
        ).paginate(page=page, per_page=10)

    @staticmethod
    def get_by_desa(desa_id, search='', page=1):
        return Jamaah.query.filter(
            Jamaah.desa_id == desa_id,
            or_(
                Jamaah.nama.like(f"%{search}%"),
                Jamaah.nik.like(f"%{search}%"),
            )
        ).paginate(page=page, per_page=10)

    @property
    def provinsi(self):
        return Provinsi.get(self.provinsi_id)

    @property
    def kabupaten(self):

        kabupaten = Kabupaten.get(self.kabupaten_id)
        return kabupaten.name if kabupaten else ""

    @kabupaten.setter
    def kabupaten(self, value):
        if type(value) is str:
            self.kabupaten_id = value

    @property
    def kecamatan(self):
        kecamatan = Kecamatan.get(self.kecamatan_id)
        return kecamatan.name if kecamatan else ""

    @kecamatan.setter
    def kecamatan(self, value):
        if type(value) is str:
            self.kecamatan_id = value

    @property
    def desa(self):
        desa = Desa.get(self.desa_id)
        return desa.name if desa else None

    @desa.setter
    def desa(self, value):
        if type(value) is str:
            self.desa_id = value
