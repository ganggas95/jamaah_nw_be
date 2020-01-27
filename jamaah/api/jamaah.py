"""Module API for jamaah"""
from flask import request
from flask_jwt_extended import jwt_required, current_user as user
from flask.views import MethodView
from jamaah.provider.jamaah_provider import JamaahProvider
from jamaah.tasks.jamaah_tasks import JamaahTasks


class JamaahAPI(MethodView):
    """Class Jamaah API"""
    jamaah_provider = JamaahProvider()


class JamaahListAPI(JamaahAPI):
    """Class API for list jamaah"""

    @jwt_required
    def get(self):
        """Method get to handle request list jamaah"""
        params = request.args
        kabupaten_id = None
        kecamatan_id = None
        # If user is admin kabupaten
        if user and user.role == 'admin kabupaten':
            kabupaten_id = user.kabupaten_id
        #  If user is admin kecamatan
        if user and user.role == 'admin kecamatan':
            kecamatan_id = user.kecamatan_id
        # Get list jamaah by kabupaten or kecamatan id
        paginate = self.jamaah_provider.list_jamaah(
            params, kabupaten_id=kabupaten_id, kecamatan_id=kecamatan_id)
        return self.jamaah_provider.create_response(
            status=200,
            data=self.jamaah_provider.jamaah_serializers.dump(paginate.items),
            meta=paginate,
        )

    @jwt_required
    def post(self):
        """Method post to handle request add new jamaah"""
        payload = request.get_json(force=True)
        jamaah = self.jamaah_provider.create_jamaah(payload)
        return self.jamaah_provider.create_response(
            status=201 if jamaah else 400,
            data=self.jamaah_provider.jamaah_serializer.dump(jamaah),
            msg="Success tambah jamaah" if jamaah else "Gagal tambah jamaah"
        )


class DetailJamaahAPI(JamaahAPI):
    """Class API for detail jamaah"""

    @jwt_required
    def get(self, jamaah_id):
        """Method get to handle get detail jamaah by id"""
        jamaah = self.jamaah_provider.get_detail(jamaah_id)
        return self.jamaah_provider.create_response(
            status=200 if jamaah else None,
            data=self.jamaah_provider.jamaah_serializer.dump(jamaah),
        )

    @jwt_required
    def put(self, jamaah_id):
        """Method put to handle update data jamaah"""
        payload = request.get_json(force=True)
        jamaah = self.jamaah_provider.update_jamaah(jamaah_id, payload)
        return self.jamaah_provider.create_response(
            status=200 if jamaah else 400,
            data=self.jamaah_provider.jamaah_serializer.dump(jamaah),
            msg="Success edit jamaah" if jamaah else "Gagal edit jamaah"
        )

    @jwt_required
    def delete(self, jamaah_id):
        """Method delete to handle delete data jamaah"""
        jamaah_id = self.jamaah_provider.delete_jamaah(jamaah_id)
        return self.jamaah_provider.create_response(
            status=200 if jamaah_id else 404,
            data=jamaah_id,
            msg="Success hapus jamaah" if jamaah_id else "Gagal Hapus jamaah"
        )


class ReportDataAPI(JamaahAPI):
    """Class API for report data jamaah"""
    @jwt_required
    def get(self):
        """Method to handle generate task"""
        task = JamaahTasks()
        kabupaten_id = None
        kecamatan_id = None
        if user and user.role == 'admin kabupaten':
            kabupaten_id = user.kabupaten_id
        if user and user.role == 'admin kecamatan':
            kecamatan_id = user.kecamatan_id

        result = task.apply_async(
            args=[None, kabupaten_id, kecamatan_id],
            queue="jamaah_tasks")
        return self.jamaah_provider.create_response(
            status=200,
            data=str(result),
            msg="Task telah dibuat",
        )
