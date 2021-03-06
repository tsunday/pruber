from datetime import datetime

from django.test import TestCase

from schedule.services import ReservationService


class ReservationTest(TestCase):
    fixtures = ['rooms.yaml', 'bands.yaml', 'schedule.yaml']

    def setUp(self) -> None:
        self.service = ReservationService()

    def test_reserved_in_time_range__start_before_start_end_before_end(self):
        reserved = self.service.get_reserved_rooms(datetime(2019, 11, 2, 15, 30), datetime(2019, 11, 2, 16, 15))
        assert list(reserved) == [1]

    def test_reserved_in_time_range__start_before_start_end_after_end(self):
        reserved = self.service.get_reserved_rooms(datetime(2019, 11, 2, 15, 30), datetime(2019, 11, 2, 17, 00))
        assert list(reserved) == [1, 2]

    def test_reserved_in_time_range__start_after_start_end_before_end(self):
        reserved = self.service.get_reserved_rooms(datetime(2019, 11, 2, 16, 15), datetime(2019, 11, 2, 16, 30))
        assert list(reserved) == [1, 2]

    def test_reserved_in_time_range__start_after_start_end_after_end(self):
        reserved = self.service.get_reserved_rooms(datetime(2019, 11, 2, 16, 15), datetime(2019, 11, 2, 16, 45))
        assert list(reserved) == [1, 2]

    def test_reserved_in_time_range__start_at_end_end_after_end(self):
        reserved = self.service.get_reserved_rooms(datetime(2019, 11, 2, 16, 30), datetime(2019, 11, 2, 16, 45))
        assert list(reserved) == [2]

    def test_reserved_in_time_range__before_or_after(self):
        before = self.service.get_reserved_rooms(datetime(2019, 11, 2, 15, 15), datetime(2019, 11, 2, 15, 30))
        after = self.service.get_reserved_rooms(datetime(2019, 11, 2, 17, 15), datetime(2019, 11, 2, 17, 30))
        assert list(before) == []
        assert list(after) == []
