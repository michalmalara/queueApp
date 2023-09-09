from unittest.mock import Mock

import pytest


@pytest.mark.django_db
class TestIsAdminOrReadOnly:
    def test_given_admin_when_request_is_post_then_return_true(self, admin_user):
        mocked_request = Mock(method="POST", user=admin_user)

        from queueService.api.permissions import IsAdminOrReadOnly
        permission = IsAdminOrReadOnly().has_permission(mocked_request, None)

        assert permission is True

    def test_given_regular_when_request_is_post_then_return_false(self, user):
        mocked_request = Mock(method="POST", user=user)

        from queueService.api.permissions import IsAdminOrReadOnly
        permission = IsAdminOrReadOnly().has_permission(mocked_request, None)

        assert permission is False

    def test_given_regular_when_request_is_get_then_return_true(self, user):
        mocked_request = Mock(method="GET", user=user)

        from queueService.api.permissions import IsAdminOrReadOnly
        permission = IsAdminOrReadOnly().has_permission(mocked_request, None)

        assert permission is True
