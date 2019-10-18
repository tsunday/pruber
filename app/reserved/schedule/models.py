from django.db import models

from bands.models import Band
from rooms.models import Room


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='reservations')
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()
