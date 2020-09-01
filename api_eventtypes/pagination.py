from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class EventTypeLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 500
    max_limit = 100

class EventTypePageNumberPagination(PageNumberPagination):
    page_size = 100
