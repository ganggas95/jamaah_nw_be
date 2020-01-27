"""Module serializers for wilayah"""
from jamaah.factory import ma
from jamaah.models.wilayah import Provinsi
from jamaah.models.wilayah import Kabupaten
from jamaah.models.wilayah import Kecamatan
from jamaah.models.wilayah import Desa


class ProvinsiSerializers(ma.ModelSchema):
    """Serializers class for provinsi"""
    class Meta:
        """Meta class"""
        model = Provinsi
        fields = ["name", "id"]


class KabupatenSerializers(ma.ModelSchema):
    """Serializers class for kabupaten"""

    class Meta:
        """Meta class"""
        model = Kabupaten


class KecamatanSerializers(ma.ModelSchema):
    """Serializers class for kecamatan"""

    class Meta:
        """Meta class"""
        model = Kecamatan


class DesaSerializers(ma.ModelSchema):
    """Serializers class for desa"""

    class Meta:
        """Meta class"""
        model = Desa
