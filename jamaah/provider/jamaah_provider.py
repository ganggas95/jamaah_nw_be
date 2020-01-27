from jamaah.provider.base import Provider
from jamaah.serializers.jamaah_serializers import Jamaah, JamaahSerailizers


class JamaahProvider(Provider):
    model = Jamaah
    jamaah_serializers = JamaahSerailizers(many=True)
    jamaah_serializer = JamaahSerailizers()

    def list_jamaah(self, params: dict, provinsi_id=None, kabupaten_id=None, kecamatan_id=None):
        paginate_jamaah = None
        search = params.get("search", default='', type=str)
        page = params.get("page", default=1, type=int)
        provinsi_id = params.get("provinsi", provinsi_id)
        kabupaten_id = params.get("kabupaten_id", kabupaten_id)
        kecamatan_id = params.get("kecamatan_id", kecamatan_id)
        if provinsi_id:
            paginate_jamaah = self.model.get_by_provinsi(
                provinsi_id, search, page)
        elif kabupaten_id:
            paginate_jamaah = self.model.get_by_kabupaten(
                kabupaten_id, search, page)
        elif kecamatan_id:
            paginate_jamaah = self.model.get_by_kecamatan(
                kecamatan_id, search, page)
        else:
            paginate_jamaah = self.model.get_all(search, page)
        return paginate_jamaah

    def get_detail(self, jamaah_id):
        return self.model.get(jamaah_id)

    def create_jamaah(self, payload: dict):
        jamaah = self.model(payload.get('nama'), payload.get('nik'))
        if jamaah.nik is None and jamaah.nama is None:
            return None
        jamaah.from_request(payload)
        jamaah.save()
        return jamaah

    def update_jamaah(self, jamaah_id, payload: dict):
        jamaah = self.model.get(jamaah_id)
        if jamaah is None:
            return None
        jamaah.from_request(payload)
        jamaah.save()
        return jamaah

    def delete_jamaah(self, jamaah_id):
        jamaah = self.model.get(jamaah_id)
        if jamaah is None:
            return None
        jamaah.delete()
        return jamaah_id
