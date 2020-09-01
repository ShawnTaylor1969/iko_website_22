from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class SpaceLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 400

class SpacePageNumberPagination(PageNumberPagination):
    page_size = 100
