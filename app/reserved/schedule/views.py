from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet

from schedule.models import Reservation
from schedule.serializers import ReservationSerializer


class ReservationViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
