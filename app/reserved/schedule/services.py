from datetime import datetime

from schedule.models import Reservation
from schedule.repository import ReservationQuerySet


class ReservationService:
    def get_reserved_rooms(self, dt_from: datetime, dt_to: datetime) -> ReservationQuerySet:
        return Reservation.objects.scheduled_between(dt_from, dt_to).values_list('room', flat=True).distinct()
