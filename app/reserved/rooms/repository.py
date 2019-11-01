from django.db.models import QuerySet


class RoomQuerySet(QuerySet):
    def available(self) -> QuerySet:
        return self.filter(reservations__isnull=True)
