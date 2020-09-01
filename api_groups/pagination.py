from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class GroupLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 400

class GroupPageNumberPagination(PageNumberPagination):
    page_size = 100
