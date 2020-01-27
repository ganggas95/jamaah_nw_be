"""Module API for request administrative wilayah NTB"""
from flask.views import MethodView
from jamaah.provider.wilayah_provider import WilayahProvider


class ProvinsiAPI(MethodView):
    wilayah_provider = WilayahProvider()

    def get(self):
        """Method to handle get data provinsi"""
        return self.wilayah_provider.create_response(
            status=200,
            data=self.wilayah_provider.list_provinsi(),
            msg="Success"
        )


class KabupatenAPI(MethodView):
    wilayah_provider = WilayahProvider()

    def get(self):
        """Method to handle get data kabupaten"""
        return self.wilayah_provider.create_response(
            status=200,
            data=self.wilayah_provider.list_kabupaten(52),
            msg="Success"
        )


class KecamatanAPI(MethodView):
    wilayah_provider = WilayahProvider()

    def get(self, kode_kab):
        """Method to handle get data kecamatan"""
        return self.wilayah_provider.create_response(
            status=200,
            data=self.wilayah_provider.list_kecamatan(kode_kab),
            msg="Success"
        )


class DesaAPI(MethodView):
    wilayah_provider = WilayahProvider()

    def get(self, kode_kec):
        """Method to handle get data desa"""
        return self.wilayah_provider.create_response(
            status=200,
            data=self.wilayah_provider.list_desa(kode_kec),
            msg="Success"
        )
