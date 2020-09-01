from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class PositionLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 50
    max_limit = 100

class PositionPageNumberPagination(PageNumberPagination):
    page_size = 50
