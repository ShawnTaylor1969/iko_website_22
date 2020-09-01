from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class AlbumLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 500
    max_limit = 100

class AlbumPageNumberPagination(PageNumberPagination):
    page_size = 100
