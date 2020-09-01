from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class SpaceLinkLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 40

class SpaceLinkPageNumberPagination(PageNumberPagination):
    page_size = 20
