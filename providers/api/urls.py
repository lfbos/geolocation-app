from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from providers.api.viewsets import LanguageAPIView, CurrencyAPIView, ProviderViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = "api_providers"


router.register(r"", ProviderViewSet, basename="provider")

urlpatterns = [
    path("languages", LanguageAPIView.as_view(), name="languages"),
    path("currencies", CurrencyAPIView.as_view(), name="currencies"),
] + router.urls
