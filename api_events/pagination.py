from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class EventLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 500
    max_limit = 100

class EventPageNumberPagination(PageNumberPagination):
    page_size = 100
