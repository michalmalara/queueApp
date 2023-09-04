from django.contrib import admin

from queueService.models import Station, Case, Queue


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    list_display = ('case', 'datetime_created', 'datetime_completed', 'is_completed', 'station')
