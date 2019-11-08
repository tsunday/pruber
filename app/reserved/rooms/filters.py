from datetime import datetime

from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request


class AvailabilityFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet, view) -> QuerySet:
        try:
            dt_from = datetime.fromisoformat(request.query_params.get('from', ''))
            dt_to = datetime.fromisoformat(request.query_params.get('to', ''))
        except ValueError as e:
            raise ValidationError(str(e))
        return queryset.available(dt_from=dt_from, dt_to=dt_to)
