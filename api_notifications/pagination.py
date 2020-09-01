from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class NotificationLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 500

class NotificationPageNumberPagination(PageNumberPagination):
    page_size = 100
