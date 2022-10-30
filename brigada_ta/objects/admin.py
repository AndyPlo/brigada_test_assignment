from django.contrib import admin

from .models import Brigada, City, Object


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name',)


@admin.register(Brigada)
class BrigadaAdmin(admin.ModelAdmin):
    list_display = (
        'brigada_name',
        'people_amount',
        'name_responsible',
        'position_responsible',
        'rank_responsible',
        'city',
    )


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = (
        'object_name',
        'people_amount',
        'name_responsible',
        'position_responsible',
        'rank_responsible',
        'brigada',
        'city',
    )
