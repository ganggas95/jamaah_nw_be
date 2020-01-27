from flask import request
from flask_jwt_extended import current_user as user
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from jamaah.utils.wrapper import requires_groups
from jamaah.provider.user_provider import UsersProvider


class UserAPI(MethodView):
    user_provider = UsersProvider()


class UserListAPI(UserAPI):

    @jwt_required
    @requires_groups("super admin")
    def get(self):
        params = request.args
        paginate = self.user_provider.list_users(params)
        return self.user_provider.create_response(
            status=200,
            data=self.user_provider.user_serializers.dump(paginate.items),
            meta=paginate,
        )

    @jwt_required
    @requires_groups("super admin")
    def post(self):
        payload = request.get_json(force=True)
        data_user = self.user_provider.create_user(payload)
        return self.user_provider.create_response(
            status=201 if data_user else 400,
            data=self.user_provider.user_serializer.dump(data_user),
            msg="Success tambah user" if data_user else "Gagal tambah user"
        )


class DetailUserAPI(UserAPI):
    @jwt_required
    @requires_groups("super admin")
    def get(self, user_id):
        data_user = self.user_provider.get_detail(user_id)
        return self.user_provider.create_response(
            status=200 if data_user else None,
            data=self.user_provider.user_serializer.dump(data_user),
        )

    @jwt_required
    @requires_groups("super admin")
    def put(self, user_id):
        payload = request.get_json(force=True)
        data_user = self.user_provider.update_user(user_id, payload)
        return self.user_provider.create_response(
            status=200 if data_user else 400,
            data=self.user_provider.user_serializer.dump(data_user),
            msg="Success edit user" if data_user else "Gagal edit user"
        )

    @jwt_required
    @requires_groups("super admin")
    def delete(self, user_id):
        user_id = self.user_provider.delete_user(user_id)
        return self.user_provider.create_response(
            status=200 if user_id else 404,
            data=user_id,
            msg="Success hapus user" if user_id else "Gagal Hapus user"
        )


class ResetPasswordAPI(UserAPI):
    @jwt_required
    @requires_groups("super admin")
    def get(self, user_id):
        data_user = self.user_provider.reset_password(user_id)
        return self.user_provider.create_response(
            status=200 if data_user else 400,
            data=self.user_provider.user_serializer.dump(data_user),
            msg="Success reset password" if user else "Gagal reset password"
        )


class ToggleStatusAPI(UserAPI):
    @jwt_required
    @requires_groups("super admin")
    def get(self, user_id):
        user = self.user_provider.toggle_status(user_id)
        return self.user_provider.create_response(
            status=200 if user else 400,
            data=self.user_provider.user_serializer.dump(user),
            msg="Success change status" if user else "Gagal change status"
        )


class ProfileChangePasswordAPI(UserAPI):
    @jwt_required
    def put(self):
        payload = request.get_json(force=True)
        data_user = self.user_provider.update_password(user.uid, payload)
        return self.user_provider.create_response(
            status=200 if data_user else 400,
            data=self.user_provider.user_serializer.dump(data_user),
            msg="Success edit user" if user else "Gagal edit user"
        )

    @jwt_required
    def post(self):
        payload = request.get_json(force=True)
        correct = self.user_provider.check_password(user.uid, payload)
        return self.user_provider.create_response(
            status=200 if correct else 400,
            data=correct,
            msg="Password Benar" if correct else "Password salah"
        )


class ProfileUserAPI(UserAPI):
    @jwt_required
    def put(self):
        payload = request.get_json(force=True)
        data_user = self.user_provider.update_user(user.uid, payload)
        return self.user_provider.create_response(
            status=200 if data_user else 400,
            data=self.user_provider.user_serializer.dump(data_user),
            msg="Success edit user" if user else "Gagal edit user"
        )
