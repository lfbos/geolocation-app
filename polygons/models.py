from django.db import models
from django.contrib.gis.db import models as gis_models
from utils.models import CommonInfo


class ServiceArea(CommonInfo):
    name = models.CharField(
        max_length=128,
        verbose_name='service area name'
    )
    price = models.FloatField(
        verbose_name='service area price'
    )
    provider = models.ForeignKey(
        'providers.Provider',
        related_name='service_areas',
        on_delete=models.CASCADE,
        verbose_name='provider'
    )
    polygon = gis_models.PolygonField(verbose_name='polygon')

    class Meta:
        verbose_name = "service area"
        verbose_name_plural = "service areas"

    def __str__(self):
        return self.name
