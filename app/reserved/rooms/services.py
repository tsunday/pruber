from datetime import datetime

from rooms.models import Room
from schedule.services import ReservationService


class RoomService:
    def get_available_rooms(self, dt_from: datetime, dt_to: datetime):
        return Room.objects.exclude(id__in=ReservationService().get_reserved_rooms(dt_from, dt_to))