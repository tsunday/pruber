from rest_framework.viewsets import ModelViewSet

from rooms.filters import AvailabilityFilterBackend
from rooms.models import Room
from rooms.serializers import RoomSerializer


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class EmptyRoomViewset(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [AvailabilityFilterBackend]