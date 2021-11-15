from polygons.api.serializers import ServiceAreaSerializer, ServiceAreaReadSerializer
from polygons.models import ServiceArea
from utils.viewsets import BaseViewSet


class ServiceAreaViewSet(BaseViewSet):
    queryset = ServiceArea.objects.select_related("provider__language", "provider__currency").all()
    serializer_classes = {"list": ServiceAreaReadSerializer, "retrieve": ServiceAreaReadSerializer}
    default_serializer_class = ServiceAreaSerializer
