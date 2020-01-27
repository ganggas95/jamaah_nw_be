from jamaah.factory import ma
from jamaah.serializers.wilayah_serializers import ProvinsiSerializers
from jamaah.serializers.wilayah_serializers import KabupatenSerializers
from jamaah.serializers.wilayah_serializers import KecamatanSerializers
from jamaah.serializers.wilayah_serializers import DesaSerializers
from jamaah.models.jamaah import Jamaah


class JamaahSerailizers(ma.ModelSchema):
    class Meta:
        model = Jamaah
        fields = [
            "id",
            "no_induk",
            "nama",
            "nik",
            "tempat_lahir",
            "tanggal_lahir",
            "jenis_kelamin",
            "alamat",
            "kabupaten_id",
            "kecamatan_id",
            "desa_id",
            "kabupaten",
            "kecamatan",
            "desa",
            "dusun",
            "aktif",
        ]
