"""Module for handle serializer pagination"""
from jamaah.factory import ma

class PaginationSerializer(ma.Schema):
    """Pagination serializers"""

    class Meta:
        """Meta class"""
        fields = [
            "per_page",
            "pages",
            "total",
            "page",
            "has_next",
            "next_num",
            "has_prev",
            "prev_num"
        ]
