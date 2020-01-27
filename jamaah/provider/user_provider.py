from datetime import datetime
from jamaah.provider.base import Provider
from jamaah.serializers.user_serializers import Users, UserSerializers


class UsersProvider(Provider):
    model = Users
    user_serializers = UserSerializers(many=True)
    user_serializer = UserSerializers()

    def list_users(self, params: dict):
        search = params.get("search", default='', type=str)
        page = params.get("page", default=1, type=int)
        paginate = self.model.get_list_users(search, page)
        return paginate

    def get_detail(self, user_id):
        return self.model.get(user_id)

    def create_user(self, payload: dict):
        user = self.model(payload.get('username'), payload.get('email'))
        if user.username is None and user.email is None:
            return None
        user.from_request(payload)
        user.save()
        return user
    
    def check_password(self, user_id, payload):
        user = self.model.get(user_id)
        if user is None:
            return None
        if user.check_password(payload["password"]):
            return True
        return False
    
    def reset_password(self, user_id):
        user = self.model.get(user_id)
        if user is None:
            return None
        user.password = "wirid{}".format(datetime.now().year)
        user.save()
        return user
    
    def toggle_status(self, user_id):
        user = self.model.get(user_id)
        if user is None:
            return None
        user.active = not user.active
        user.save()
        return user

    def update_user(self, user_id, payload: dict):
        user = self.model.get(user_id)
        if user is None:
            return None
        user.from_request(payload)
        user.save()
        return user
    
    def update_password(self, user_id, payload: dict):
        user = self.model.get(user_id)
        if user is None:
            return None
        if "new_password" not in payload or "conf_password" not in payload:
            return None
        if payload["new_password"] != payload["conf_password"]:
            return None
        user.password = payload["new_password"]
        user.save()
        return user

    def delete_user(self, user_id):
        user = self.model.get(user_id)
        if user is None:
            return None
        user.delete()
        return user_id
