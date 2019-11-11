from datetime import datetime

from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request

from rooms.services import RoomService


class AvailabilityFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset: QuerySet, view):
        from_param = request.query_params.get('from', '')
        to_param = request.query_params.get('to', '')
        if not (from_param and to_param):
            raise ValidationError("Missing 'from' or 'to' query parameter")
        try:
            dt_from = datetime.fromisoformat(from_param)
            dt_to = datetime.fromisoformat(to_param)
        except ValueError as e:
            raise ValidationError(str(e))
        return RoomService().get_available_rooms(dt_from=dt_from, dt_to=dt_to)
