from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from queueService.views import StationViewSet, CaseViewSet, QueueViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

router = SimpleRouter()
router.register("queue", QueueViewSet, basename="queue")
router.register("stations", StationViewSet, basename="stations")
router.register("case", CaseViewSet, basename="case")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
# urlpatterns += [
#     path("stations/remove-user/", remove_user_from_station, name="stations"),
#     path("stations/<int:pk>/assign/", assign_user_to_station, name="stations"),
# ]

urlpatterns += router.urls

# automatic api documentation urls
urlpatterns += [
    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
