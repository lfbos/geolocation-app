from rest_framework import serializers

from polygons.models import ServiceArea
from providers.api.serializers import ProviderReadSerializer


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ("id", "name", "price", "provider", "area")


class ServiceAreaReadSerializer(serializers.ModelSerializer):
    provider = ProviderReadSerializer()

    class Meta:
        model = ServiceArea
        fields = ("id", "name", "price", "provider", "area")
