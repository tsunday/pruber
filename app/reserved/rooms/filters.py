from django.db.models import QuerySet
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request


class AvailabilityFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet, view) -> QuerySet:
        return queryset.available(
            dt_from=request.query_params.get('from', None), dt_to=request.query_params.get('to', None)
        )
