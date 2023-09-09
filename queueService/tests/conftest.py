import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from queueService.models import Station, Queue, Case

user_data = {
    "username": "testuser",
    "password": "12345",
}

user2_data = {
    "username": "testuser2",
    "password": "12345",
}

admin_data = {
    "username": "admin",
    "password": "12345",
}


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(**user_data)


@pytest.fixture
def user2():
    return User.objects.create_user(**user2_data)


@pytest.fixture
def admin_user():
    return User.objects.create_superuser(**admin_data)


@pytest.fixture
def empty_station():
    return Station.objects.create(name="Test Empty Station")


@pytest.fixture
def occupied_station(user):
    return Station.objects.create(name="Test Occupied Station", user=user)


@pytest.fixture
def case(empty_station):
    case = Case.objects.create(name="First Case", symbol="A")
    case.stations.set([empty_station])
    case.save()
    return case


@pytest.fixture
def case2(occupied_station):
    case = Case.objects.create(name="Second Case", symbol="B")
    case.stations.set([occupied_station])
    case.save()
    return case


@pytest.fixture
def new_queue(case):
    return Queue.objects.create(case=case, number=1)
