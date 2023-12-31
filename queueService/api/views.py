from django.utils import timezone
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from queueService.api.permissions import IsAdminOrReadOnly
from queueService.api.serializers import StationSerializer, CaseSerializer, \
    QueueSerializer
from queueService.models import Station, Case, Queue
from queueService.notification_provider.websockets_notification_provider import WebsocketsNotificationProvider
from queueService.tasks import update_queues_info
from queueService.utils import get_or_404, get_other_queues_info


class StationViewSet(ModelViewSet):
    queryset = Station.objects.all().order_by("id")
    serializer_class = StationSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer(self, *args, **kwargs):
        if self.action == "get_current_station":
            return StationSerializer(*args, **kwargs)
        return StationSerializer(*args, **kwargs)

    @action(methods=["GET"], detail=False, url_path="available-stations")
    def get_available_stations(self, request: Request):
        available_stations = Station.objects.filter(user=None)
        serializer = self.get_serializer(available_stations, many=True)
        return Response(serializer.data)

    @action(methods=["POST"], detail=True, url_path="assign", permission_classes=[IsAuthenticated])
    def assign_user_to_station(self, request: Request, pk: int):
        station = get_or_404(Station, pk=pk)

        if station.user is not None:
            return Response({"status": "error", "message": "Station is already taken"}, status=400)

        user_station = Station.objects.filter(user=request.user)
        if user_station.exists():
            return Response({"status": "error", "message": "User already has a station"}, status=400)

        station.user = request.user
        station.save()
        return Response({"status": "ok"})

    @action(methods=["POST"], detail=False, url_path="remove-user", permission_classes=[IsAuthenticated])
    def remove_user_from_station(self, request: Request):
        station = get_or_404(Station, user=request.user)

        current_queues = Queue.objects.filter(station=station, is_completed=False)

        if len(current_queues):
            for queue in current_queues:
                queue.datetime_completed = timezone.now()
                queue.is_completed = True
                queue.station = None
                queue.save()

        station.user = None
        station.save()
        return Response({"status": "ok"})

    @action(methods=["GET"], detail=False, url_path="current", permission_classes=[IsAuthenticated])
    def get_current_station(self, request: Request):
        station = get_or_404(Station, user=request.user)

        return Response(StationSerializer(station, many=False).data)


class CaseViewSet(ModelViewSet):
    queryset = Case.objects.all().order_by("id")
    serializer_class = CaseSerializer
    permission_classes = (IsAdminOrReadOnly,)


class QueueViewSet(ViewSet, mixins.CreateModelMixin):
    queryset = Case.objects.all().order_by("id")
    permission_classes = (IsAuthenticated,)
    serializer_class = QueueSerializer

    notifications_provider = WebsocketsNotificationProvider()

    def get_serializer(self, *args, **kwargs):
        return QueueSerializer(*args, **kwargs)

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            queue = serializer.create(serializer.validated_data)
            response_data = get_other_queues_info(queue)
            return Response(status=201, data=response_data)
        return Response({"status": "error", "message": serializer.errors}, status=422)

    @action(methods=["POST"], detail=False, url_path="call-next", permission_classes=[IsAuthenticated])
    def call_next(self, request: Request):
        station = get_or_404(Station, user=request.user)
        cases = station.cases.all()
        current_queues = Queue.objects.filter(station=station, is_completed=False)

        if len(current_queues):
            for queue in current_queues:
                queue.datetime_completed = timezone.now()
                queue.is_completed = True
                queue.station = None
                queue.save()

        next_queue = Queue.objects.filter(is_completed=False, case__in=cases).order_by("number").first()
        if next_queue is not None:
            next_queue.station = station
            next_queue.datetime_started = timezone.now()
            next_queue.save()

            response_data = get_other_queues_info(next_queue)

            update_queues_info.delay()

            return Response(response_data)

        return Response({"status": "error", "message": "No cases in queue"}, status=400)

    @action(methods=["GET"], detail=True, url_path="details", permission_classes=[AllowAny])
    def get_queue_details(self, request: Request, pk: int):
        queue = get_or_404(Queue, pk=pk)

        return Response(get_other_queues_info(queue))

    @action(methods=["GET"], detail=False, url_path="current", permission_classes=[AllowAny])
    def get_current_queue(self, request: Request):
        queue = get_or_404(
            Queue,
            datetime_started__isnull=False,
            datetime_completed__isnull=True,
            is_completed=False
        )

        return Response(get_other_queues_info(queue))

    @action(methods=["POST"], detail=False, url_path="complete", permission_classes=[IsAuthenticated])
    def complete_queue(self, request: Request):
        station = get_or_404(Station, user=request.user)

        queue = get_or_404(Queue, station=station, is_completed=False)

        queue.datetime_completed = timezone.now()
        queue.is_completed = True
        queue.station = None
        queue.save()

        return Response(get_other_queues_info(queue))
