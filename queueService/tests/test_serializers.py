import pytest

from queueService.api.serializers import StationSerializer, QueueSerializer


@pytest.mark.django_db
class TestStationRetrieveSerializer:
    def test_given_empty_station_when_retrieve_station_is_active_false(self, empty_station):
        serializer = StationSerializer(empty_station)
        assert serializer.data['is_active'] is False

    def test_given_occupied_station_when_retrieve_station_is_active_true(self, occupied_station):
        serializer = StationSerializer(occupied_station)
        assert serializer.data['is_active'] is True


@pytest.mark.django_db
class TestQueueSerializer:
    def test_given_case_when_queue_created_queue_has_next_number(self, case):
        queue_data = {
            "case": case.id
        }

        serializer = QueueSerializer(data=queue_data)
        serializer.is_valid(raise_exception=True)
        queue = serializer.create(serializer.validated_data)
        assert queue.number == 1

    def test_given_case_and_queue_when_queue_created_queue_has_next_number(self, case, new_queue):
        queue_data = {
            "case": case.id
        }

        serializer = QueueSerializer(data=queue_data)
        serializer.is_valid(raise_exception=True)
        queue = serializer.create(serializer.validated_data)
        assert queue.number == new_queue.number + 1

    def test_given_case_and_queue2_when_queue_created_queue_has_next_number(self, case, new_queue2):
        queue_data = {
            "case": case.id
        }

        serializer = QueueSerializer(data=queue_data)
        serializer.is_valid(raise_exception=True)
        queue = serializer.create(serializer.validated_data)
        assert queue.number == 1
