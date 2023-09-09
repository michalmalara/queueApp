import logging

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from queueService.models import Station, Queue


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


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = "__all__"


class QueueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = ["case"]

    def create(self, validated_data):
        last_number = Queue.objects.filter(case=validated_data.get("case")).order_by("-number").first()
        queue = Queue.objects.create(**validated_data)
        queue.number = last_number.number + 1 if last_number is not None else 1
        queue.save()
        return queue


class QueueRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = ["id", "case", "number"]
