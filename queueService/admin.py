from django.contrib import admin

from queueService.models import Station, Case


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('name',)
