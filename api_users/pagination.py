from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 50
    max_limit = 300

class UserPageNumberPagination(PageNumberPagination):
    page_size = 50
