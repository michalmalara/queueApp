from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def get_token_for_user(user: User) -> str:
    refresh = RefreshToken.for_user(user)

    return f"Bearer {refresh.access_token}"
