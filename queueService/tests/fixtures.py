import pytest


@pytest.fixture
def user():
    from django.contrib.auth.models import User

    return User.objects.create_user(username="testuser", password="12345")


@pytest.fixture
def admin_user():
    from django.contrib.auth.models import User

    return User.objects.create_superuser(username="admin", password="12345")


@pytest.fixture
def empty_station():
    from queueService.models import Station

    return Station.objects.create(name="Test Station")


@pytest.fixture
def occupied_station(user):
    from queueService.models import Station

    return Station.objects.create(name="Test Station", user=user)
