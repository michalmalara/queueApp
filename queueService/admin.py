from django.contrib import admin

from queueService.models import Station, Case, Queue


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user")


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    list_display = (
        "id", "case", "number", "datetime_created", "datetime_started", "datetime_completed", "is_completed", "station")
