from jamaah.factory import ma
from jamaah.models.users import Users


class UserSerializers(ma.ModelSchema):

    class Meta:
        model = Users
        fields = [
            'uid',
            'username',
            'email',
            "active",
            "role",
            "kabupaten_id",
            "kecamatan_id",
            "kabupaten",
            "kecamatan",
        ]
