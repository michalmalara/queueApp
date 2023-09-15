import pytest
from django.utils import timezone

from queueService.tests.utils import get_token_for_user


@pytest.mark.django_db
class TestAssignUserToStation:
    def test_given_station_when_assign_user_to_station_then_user_is_assigned(self, client, user, empty_station):
        response = client.post(
            f"/api/stations/{empty_station.id}/assign/",
            HTTP_AUTHORIZATION=get_token_for_user(user),
        )

        assert response.status_code == 200

    def test_given_occupied_station_when_assign_user_to_station_then_user_is_not_assigned(self, client, user2,
                                                                                          occupied_station):
        response = client.post(
            f"/api/stations/{occupied_station.id}/assign/",
            HTTP_AUTHORIZATION=get_token_for_user(user2),
        )

        assert response.status_code == 400
        assert response.json() == {"status": "error", "message": "Station is already taken"}

    def test_given_user_assigned_to_station_when_assign_user_to_station_then_400_returned(self, client, user,
                                                                                          occupied_station,
                                                                                          empty_station):
        response = client.post(
            f"/api/stations/{empty_station.id}/assign/",
            HTTP_AUTHORIZATION=get_token_for_user(user),
        )

        assert response.status_code == 400
        assert response.json() == {"status": "error", "message": "User already has a station"}


@pytest.mark.django_db
class TestRemoveUserFromStation:
    def test_given_station_with_user_when_remove_user_from_station_then_user_is_removed(self, client, user,
                                                                                        occupied_station):
        response = client.post(
            f"/api/stations/remove-user/",
            HTTP_AUTHORIZATION=get_token_for_user(user),
        )

        assert response.status_code == 200

    def test_given_user_not_assigned_when_remove_user_from_station_then_404_returned(self, client, user,
                                                                                     empty_station):
        response = client.post(
            f"/api/stations/remove-user/",
            HTTP_AUTHORIZATION=get_token_for_user(user),
        )

        assert response.status_code == 404


@pytest.mark.django_db
class TestQueueViewSet:
    def test_given_case_when_user_creates_new_queue_then_queue_is_created(self, client, user, case):
        response = client.post(
            "/api/queue/",
            {"case": case.id},
            HTTP_AUTHORIZATION=get_token_for_user(user),
        )

        assert response.status_code == 201
        assert response.json()["case"] == case.id
        assert response.json()["number"] == 1

    def test_given_case_and_queue_when_user_creates_new_queue_then_queue_is_created_and_next_number_is_assigned(
            self,
            client,
            user,
            case,
            new_queue
    ):
        response = client.post(
            "/api/queue/",
            {"case": case.id},
            HTTP_AUTHORIZATION=get_token_for_user(user),
        )

        assert response.status_code == 201
        assert response.json()["case"] == case.id
        assert response.json()["number"] == new_queue.number + 1

    def test_given_case_case2_and_queue_when_user_creates_new_queue_for_case2_then_queue_is_created(
            self,
            client,
            user,
            case,
            case2,
            new_queue
    ):
        response = client.post(
            "/api/queue/",
            {"case": case2.id},
            HTTP_AUTHORIZATION=get_token_for_user(user),
        )

        assert response.status_code == 201
        assert response.json()["case"] == case2.id
        assert response.json()["number"] == 1

    def test_given_queue_and_station_when_user_calls_next_then_queue_is_assigned_to_station(
            self,
            client,
            user,
            new_queue,
            case,
            occupied_station
    ):
        occupied_station.cases.add(case)
        occupied_station.save()

        new_queue.case = case
        new_queue.datetime_started = timezone.now()
        new_queue.save()

        response = client.post(
            "/api/queue/call-next/",
            HTTP_AUTHORIZATION=get_token_for_user(user),
        )

        assert response.status_code == 200
        assert response.json()["case"] == case.id
        assert response.json()["number"] == new_queue.number
