from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from polygons.api.viewsets import ServiceAreaViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = "api_polygons"

router.register(r"", ServiceAreaViewSet, basename="service-area")

urlpatterns = [path("", include(router.urls))]
