from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class PageDetailLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 500
    max_limit = 100

class PageDetailPageNumberPagination(PageNumberPagination):
    page_size = 100
