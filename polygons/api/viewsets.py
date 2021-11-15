from rest_framework import viewsets

from polygons.api.serializers import ServiceAreaSerializer
from polygons.models import ServiceArea


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
