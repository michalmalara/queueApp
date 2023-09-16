from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path(r'', TemplateView.as_view(template_name="templates/home.html")),
    path("admin/", admin.site.urls),
    path("api/", include("queueService.api.urls")),
]
