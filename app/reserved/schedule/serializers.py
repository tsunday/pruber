from rest_framework.serializers import ModelSerializer

from schedule.models import Reservation


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        breakpoint()
        return data
