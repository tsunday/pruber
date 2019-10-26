from django.db.models import QuerySet


class RoomQuerySet(QuerySet):
    def available(self):
        return self.filter(reservations__isnull=True)
