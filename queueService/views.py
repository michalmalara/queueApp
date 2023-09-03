from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from queueService.models import Station
from queueService.permissions import IsAdminOrReadOnly
from queueService.serializers import StationSerializer, StationRetrieveSerializer
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
def set_user_to_station(request, pk):
    station = get_or_404(Station, pk=pk)

    if station.user is not None:
        return Response({"status": "error", "message": "Station is already taken"}, status=400)

    user_station = Station.objects.filter(user=request.user)
    if user_station.exists():
        return Response({"status": "error", "message": "User already has a station"}, status=400)

    station.user = request.user
    station.save()
    return Response({"status": "ok"})
