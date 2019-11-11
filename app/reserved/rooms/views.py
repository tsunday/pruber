from django.db.models import QuerySet
from rest_framework.viewsets import ReadOnlyModelViewSet

from rooms.filters import AvailabilityFilterBackend
from rooms.models import Room
from rooms.serializers import RoomSerializer


class RoomViewSet(ReadOnlyModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class AvailableRoomViewSet(RoomViewSet):
    filter_backends = [AvailabilityFilterBackend]

