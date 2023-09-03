import pytest

from queueService.models import Station
from queueService.serializers import StationRetrieveSerializer


@pytest.mark.django_db
class TestStationRetrieveSerializer:
    def test_given_empty_station_when_retrieve_station_is_active_false(self, empty_station):
        serializer = StationRetrieveSerializer(empty_station)
        assert serializer.data['is_active'] is False

    def test_given_occupied_station_when_retrieve_station_is_active_true(self, occupied_station):
        serializer = StationRetrieveSerializer(occupied_station)
        assert serializer.data['is_active'] is True
