from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class ProgramLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10

class ProgramPageNumberPagination(PageNumberPagination):
    page_size = 2
