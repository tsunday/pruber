from datetime import datetime

from django.db.models import QuerySet


class RoomQuerySet(QuerySet):
    def available(self, dt_from: datetime, dt_to: datetime) -> QuerySet:
        print(f'Qs filtered by from: {dt_from} to: {dt_to}')
        # Reservation.objects.filter(datetime_from__lt=dt_from, datetime_to__)
        return self.filter(reservations__isnull=True)
