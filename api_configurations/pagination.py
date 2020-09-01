from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class ConfigurationLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10

class ConfigurationPageNumberPagination(PageNumberPagination):
    page_size = 2
