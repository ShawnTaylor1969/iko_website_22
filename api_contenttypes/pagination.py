from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class ContentTypeLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 500

class ContentTypePageNumberPagination(PageNumberPagination):
    page_size = 100
