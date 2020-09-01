from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class TimelineLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 500

class TimelinePageNumberPagination(PageNumberPagination):
    page_size = 100
