from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class PhotoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 500
    max_limit = 100

class PhotoPageNumberPagination(PageNumberPagination):
    page_size = 100
