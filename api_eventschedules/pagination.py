from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class EventScheduleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 500
    max_limit = 100

class EventSchedulePageNumberPagination(PageNumberPagination):
    page_size = 100
