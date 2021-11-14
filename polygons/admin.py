from django.contrib import admin

from polygons.models import ServiceArea


@admin.register(ServiceArea)
class ServiceAreaAdmin(admin.ModelAdmin):
    search_fields = ("name", "provider__email",)
    list_select_related = ("provider",)
