from django.contrib import admin
from django.urls import path, include, re_path

from queueService.urls import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("queueService.api.urls")),
    re_path(r'^(?:.*)/?$', index),
]
