from rest_framework import serializers

from polygons.models import ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ("id", "name", "price", "provider", "area")
