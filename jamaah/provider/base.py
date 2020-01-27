"""Module Provider"""
from jamaah.utils.response import create_response
from jamaah.serializers.pagination_serializers import PaginationSerializer


class Provider:
    """Provider class"""
    paginate_serialize = PaginationSerializer()

    def create_response(self, status=200, data=None, msg="", errors=None, meta=None):
        """method to handle create response"""
        if meta:
            meta = self.paginate_serialize.dump(meta)
        return create_response(status=status, data=data, msg=msg, errors=errors, meta=meta)
