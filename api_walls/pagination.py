from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class WallLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 500
    max_limit = 100

class WallPageNumberPagination(PageNumberPagination):
    page_size = 100
