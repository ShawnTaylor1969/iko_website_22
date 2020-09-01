from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class CalendarLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 500
    max_limit = 100

class CalendarPageNumberPagination(PageNumberPagination):
    page_size = 100
