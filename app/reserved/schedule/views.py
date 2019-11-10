from rest_framework.viewsets import ReadOnlyModelViewSet

from schedule.models import Reservation
from schedule.serializers import ReservationSerializer


class ReservationViewSet(ReadOnlyModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
