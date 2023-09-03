from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ExtendedTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username

        return token