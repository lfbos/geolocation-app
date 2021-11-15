from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from providers.api.serializers import LanguageSerializer, CurrencySerializer, ProviderSerializer
from providers.models import Language, Currency, Provider
from utils.viewsets import CachedListAPIView


class LanguageAPIView(CachedListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = []
    filter_backends = (SearchFilter,)
    search_fields = ("name",)


class CurrencyAPIView(CachedListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = []
    filter_backends = (SearchFilter,)
    search_fields = ("name",)


class ProviderViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
