from datetime import datetime

from django.db.models import QuerySet, Q


class ReservationQuerySet(QuerySet):
    def scheduled_between(self, dt_from: datetime, dt_to: datetime) -> QuerySet:
        return self.filter(
            Q(datetime_from__lte=dt_from, datetime_to__lte=dt_to, datetime_to__gt=dt_from) |
            Q(datetime_from__gte=dt_from, datetime_from__lt=dt_to)
        )
