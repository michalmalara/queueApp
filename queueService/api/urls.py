from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from queueApp import settings
from queueService.api.views import StationViewSet, CaseViewSet, QueueViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Queue Service API",
        default_version="v1",
        description="API for Queue Service",
        contact=openapi.Contact(email="michalmalara@gmailcom"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny] if settings.DEBUG else [permissions.IsAuthenticated],
)

router = SimpleRouter()
router.register("queue", QueueViewSet, basename="queue")
router.register("stations", StationViewSet, basename="stations")
router.register("case", CaseViewSet, basename="case")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # automatic api documentation urls

    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns += router.urls
