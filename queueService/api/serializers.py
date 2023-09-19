from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from queueService.models import Station, Queue, Case


class ExtendedTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username

        return token


class StationSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Station
        fields = ["id", "name", "is_active"]
        read_only_fields = ["id", "is_active"]

    @staticmethod
    def get_is_active(obj):
        return obj.user is not None


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ["id", "name", "symbol", "description"]


class QueueSerializer(serializers.ModelSerializer):
    case_symbol = serializers.SerializerMethodField()
    case_name = serializers.SerializerMethodField()

    class Meta:
        model = Queue
        fields = ["id", "case", "case_symbol", "case_name", "number", "datetime_created", "datetime_started",
                  "datetime_completed", "is_completed", "station"]
        read_only_fields = ["id", "number", "datetime_created", "datetime_started", "datetime_completed", "station",
                            "is_completed"]

    def get_case_symbol(self, obj):
        return obj.case.symbol

    def get_case_name(self, obj):
        return obj.case.name

    def create(self, validated_data):
        last_number = Queue.objects.filter(case=validated_data.get("case")).order_by("-number").first()
        queue = Queue.objects.create(**validated_data)
        queue.number = last_number.number + 1 if last_number is not None else 1
        queue.save()
        return queue
