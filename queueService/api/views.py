from django.utils import timezone
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from queueService.models import Station, Case, Queue
from queueService.api.permissions import IsAdminOrReadOnly
from queueService.api.serializers import StationSerializer, StationRetrieveSerializer, CaseSerializer, \
    QueueCreateSerializer, QueueRetrieveSerializer
from queueService.utils import get_or_404


class StationViewSet(ModelViewSet):
    queryset = Station.objects.all().order_by("id")
    serializer_class = StationSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ("get", "list", "retrieve"):
            return StationRetrieveSerializer
        return StationSerializer

    @action(methods=["POST"], detail=True, url_path="assign", permission_classes=[IsAuthenticated])
    def assign_user_to_station(self, request, pk):
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
    def remove_user_from_station(self, request):
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


class CaseViewSet(ModelViewSet):
    queryset = Case.objects.all().order_by("id")
    serializer_class = CaseSerializer
    permission_classes = (IsAdminOrReadOnly,)


class QueueViewSet(ViewSet, mixins.CreateModelMixin):
    queryset = Case.objects.all().order_by("id")
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        if self.action == "create":
            return QueueCreateSerializer(*args, **kwargs)
        return QueueRetrieveSerializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            queue = serializer.create(serializer.validated_data)
            return Response(status=201, data=QueueRetrieveSerializer(queue).data)
        return Response({"status": "error", "message": serializer.errors}, status=422)

    @action(methods=["POST"], detail=False, url_path="call-next", permission_classes=[IsAuthenticated])
    def call_next(self, request):
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
            return Response(QueueRetrieveSerializer(next_queue).data)

        return Response({"status": "error", "message": "No cases in queue"}, status=400)

    @action(methods=["GET"], detail=False, url_path="current", permission_classes=[IsAuthenticated])
    def get_current_queue(self, request):
        queues = Queue.objects.filter(
            datetime_started__isnull=False,
            datetime_completed__isnull=True,
            is_completed=False
        )
        if queues.exists():
            return Response(QueueRetrieveSerializer(queues.first()).data)
        return Response({"status": "error", "message": "No current queue"}, status=400)
