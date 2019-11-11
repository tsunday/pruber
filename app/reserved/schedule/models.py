from django.db import models

from bands.models import Band
from rooms.models import Room
from schedule.repository import ReservationQuerySet


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='reservations')
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()

    objects = ReservationQuerySet.as_manager()
