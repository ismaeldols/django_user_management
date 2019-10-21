from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django.conf import settings


DEFAULT_MAX_PAGE_SIZE = 100


class CustomLimitOffsetPagination(LimitOffsetPagination):
    max_limit = getattr(settings, 'REST_FRAMEWORK', {}).get('PAGE_SIZE', DEFAULT_MAX_PAGE_SIZE)
    limit_query_description = 'Number of results to return. Maximum number is {max_limit}.'.format(max_limit=max_limit)

    def get_paginated_response(self, data):
        return Response(data)
