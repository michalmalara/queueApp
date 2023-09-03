from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from queueService.models import Station


class ExtendedTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username

        return token


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = "__all__"


class StationRetrieveSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Station
        fields = ("name", "is_active")

    @staticmethod
    def get_is_active(obj):
        return obj.user is not None
