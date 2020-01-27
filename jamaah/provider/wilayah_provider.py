from jamaah.provider.base import Provider
from jamaah.serializers.wilayah_serializers import Desa
from jamaah.serializers.wilayah_serializers import Provinsi
from jamaah.serializers.wilayah_serializers import Kabupaten
from jamaah.serializers.wilayah_serializers import Kecamatan
from jamaah.serializers.wilayah_serializers import ProvinsiSerializers
from jamaah.serializers.wilayah_serializers import KabupatenSerializers
from jamaah.serializers.wilayah_serializers import KecamatanSerializers
from jamaah.serializers.wilayah_serializers import DesaSerializers


class WilayahProvider(Provider):
    provinsi_serializers = ProvinsiSerializers(many=True)
    kabupaten_serializers = KabupatenSerializers(many=True)
    kecamatan_serializers = KecamatanSerializers(many=True)
    desa_serializers = DesaSerializers(many=True)

    def list_provinsi(self):
        _list_provinsi = Provinsi.get_all()
        return self.provinsi_serializers.dump(_list_provinsi)

    def list_kabupaten(self, kode_prov):
        _list_kabupaten = Kabupaten.get_by_provinsi(str(kode_prov))
        return self.kabupaten_serializers.dump(_list_kabupaten)

    def list_kecamatan(self, kode_kab):
        _list_kecamatan = Kecamatan.get_by_kabupaten(kode_kab)
        return self.kecamatan_serializers.dump(_list_kecamatan)

    def list_desa(self, kode_kec):
        _list_desa = Desa.get_by_desa(kode_kec)
        return self.desa_serializers.dump(_list_desa)
