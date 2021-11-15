import django_filters as filters
from django.contrib.gis.geos import Point

from polygons.models import ServiceArea
from utils import is_float


class ServiceAreaFilter(filters.FilterSet):
    lat = filters.NumberFilter(method="point_filter")
    lng = filters.NumberFilter(method="point_filter")

    class Meta:
        model = ServiceArea
        fields = ("name", "price", "lat", "lng")

    def point_filter(self, queryset, name, value):
        lat = self.request.query_params.get("lat", "")
        lng = self.request.query_params.get("lng", "")
        if is_float(lat) and is_float(lng):
            latitude = float(lat)
            longitude = float(lng)
            point = Point(latitude, longitude)
            return queryset.filter(area__contains=point)

        return queryset
