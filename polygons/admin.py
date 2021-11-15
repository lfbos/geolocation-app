from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from polygons.models import ServiceArea


@admin.register(ServiceArea)
class ServiceAreaAdmin(OSMGeoAdmin):
    search_fields = (
        "name",
        "provider__email",
    )
    list_select_related = ("provider",)
