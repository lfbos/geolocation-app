from rest_framework.filters import SearchFilter

from providers.api.serializers import (
    LanguageSerializer,
    CurrencySerializer,
    ProviderSerializer,
    ProviderReadSerializer,
)
from providers.models import Language, Currency, Provider
from utils.viewsets import CachedListAPIView, BaseViewSet


class LanguageAPIView(CachedListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = []
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    pagination_class = None


class CurrencyAPIView(CachedListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = []
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    pagination_class = None


class ProviderViewSet(BaseViewSet):
    queryset = Provider.objects.select_related("language", "currency").order_by("-created_at")
    serializer_classes = {"list": ProviderReadSerializer, "retrieve": ProviderReadSerializer}
    default_serializer_class = ProviderSerializer
