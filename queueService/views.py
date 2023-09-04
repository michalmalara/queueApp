from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from queueService.models import Station, Case
from queueService.permissions import IsAdminOrReadOnly
from queueService.serializers import StationSerializer, StationRetrieveSerializer, CaseSerializer
from queueService.utils import get_or_404


class StationViewSet(ModelViewSet):
    queryset = Station.objects.all().order_by("id")
    serializer_class = StationSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ("get", "list", "retrieve"):
            return StationRetrieveSerializer
        return StationSerializer


@api_view(["POST"])
def assign_user_to_station(request, pk):
    station = get_or_404(Station, pk=pk)

    if station.user is not None:
        return Response({"status": "error", "message": "Station is already taken"}, status=400)

    user_station = Station.objects.filter(user=request.user)
    if user_station.exists():
        return Response({"status": "error", "message": "User already has a station"}, status=400)

    station.user = request.user
    station.save()
    return Response({"status": "ok"})


@api_view(["POST"])
def remove_user_from_station(request):
    station = get_or_404(Station, user=request.user)

    station.user = None
    station.save()
    return Response({"status": "ok"})


class CaseViewSet(ModelViewSet):
    queryset = Case.objects.all().order_by("id")
    serializer_class = CaseSerializer
    permission_classes = (IsAdminOrReadOnly,)