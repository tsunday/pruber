from django.db import models

from rooms.repository import RoomQuerySet


class City(models.Model):
    id = models.CharField(max_length=2, primary_key=True)

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'cities'


class Building(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True, blank=True)


class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    gear_description = models.CharField(max_length=255)

    objects = RoomQuerySet.as_manager()