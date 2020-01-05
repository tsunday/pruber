from datetime import datetime

from django.db.models import QuerySet

from rooms.models import Room
from schedule.services import ReservationService


class RoomService:
    def get_available_rooms(self, dt_from: datetime, dt_to: datetime) -> QuerySet:
        return Room.objects.exclude(id__in=ReservationService().get_reserved_rooms(dt_from, dt_to))
