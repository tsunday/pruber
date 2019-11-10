import datetime

from django.db.models import QuerySet, Q


class ScheduleQuerySet(QuerySet):
    def reserved_rooms(self, dt_from: datetime, dt_to: datetime):
        return self.filter(
            Q(datetime_from__lt=dt_to, datetime_to__gte=dt_to)
        ).values_list('room').distinct()
