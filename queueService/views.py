from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from queueService.models import Station, Case
from queueService.permissions import IsAdminOrReadOnly
from queueService.serializers import StationSerializer, StationRetrieveSerializer, CaseSerializer, \
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

    def get_permissions(self):
        if self.action in ("list", "retrieve", "create"):
            return (IsAuthenticated(),)
        return (IsAdminOrReadOnly(),)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            queue = serializer.create(serializer.validated_data)
            return Response(status=201, data=QueueRetrieveSerializer(queue).data)
        return Response({"status": "error", "message": serializer.errors}, status=422)

# @api_view(["GET"])
# def call_next(request):
#     station = get_or_404(Station, user=request.user)
#     current_queue = Queue.objects.filter(station=station, is_completed=False)
#     if len(current_queue):
#         current_queue[0].is_completed = True
#         current_queue[0].station = None
#         current_queue[0].save()
#
#     if station.queue_set.filter(is_completed=False).exists():
#         next_case = station.queue_set.filter(is_completed=False).order_by("datetime_created").first()
#         next_case.station = station
#         next_case.save()
#         return Response({"status": "ok", "case": CaseSerializer(next_case).data})
#     return Response({"status": "error", "message": "No cases in queue"}, status=400)
