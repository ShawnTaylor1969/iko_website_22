from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class MemberLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 50
    max_limit = 2000

class MemberPageNumberPagination(PageNumberPagination):
    page_size = 50
