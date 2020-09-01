from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10

class ArticlePageNumberPagination(PageNumberPagination):
    page_size = 2
