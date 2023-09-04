import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from queueService.models import Station

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
