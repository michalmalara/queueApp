import pytest

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
