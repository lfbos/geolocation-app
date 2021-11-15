from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet


class CachedListAPIView(ListAPIView):
    @method_decorator(cache_page(settings.CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class BaseViewSet(ModelViewSet):
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    class Meta:
        abstract = True
