import json
import os
import random
from pathlib import Path

import factory
from django.contrib.gis.geos import GEOSGeometry
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APITestCase

from polygons.models import ServiceArea
from providers.tests import ProviderFactory

generator = Factory.create()
base_dir = Path(__file__).resolve().parent
with open(os.path.join(base_dir, "coordinates.json")) as f:
    coordinates_data = json.load(f)


def get_random_coordinates():
    coordinates = random.choice(coordinates_data)
    data = {"type": "Polygon", "coordinates": coordinates.get("coordinates")}
    return data


def generate_polygon():
    data = get_random_coordinates()
    return GEOSGeometry(json.dumps(data))


class ServiceAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ServiceArea

    name = generator.word()
    price = random.uniform(0.1, 10000)
    provider = factory.SubFactory(ProviderFactory)
    area = factory.LazyFunction(generate_polygon)


class ServiceAreaTestCases(APITestCase):
    fixtures = ("languages", "currencies")

    def setUp(self) -> None:
        self.service_areas = ServiceAreaFactory.create_batch(50)

    def test_service_area_list(self):
        response = self.client.get(f'{reverse("api_polygons:service-area-list")}?page_size=30')
        results = response.json().get("results")

        self.assertEqual(len(results), 30)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_service_area_list_with_filter(self):
        point_inside_polygon = coordinates_data[0].get("points_inside")[0]
        point_outside_polygon = coordinates_data[0].get("points_outside")[0]

        query_params = f"?page_size=30&lat={point_inside_polygon[0]}&lng={point_inside_polygon[1]}"
        url = f'{reverse("api_polygons:service-area-list")}{query_params}'

        response = self.client.get(url)

        results = response.json().get("results")

        self.assertTrue(len(results) > 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        query_params = (
            f"?page_size=30&lat={point_outside_polygon[0]}&lng={point_outside_polygon[1]}"
        )
        url = f'{reverse("api_polygons:service-area-list")}{query_params}'

        response = self.client.get(url)

        results = response.json().get("results")
        self.assertFalse(len(results) > 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_service_area_with_missing_data(self):
        body = {"name": generator.word()}
        response = self.client.post(reverse("api_polygons:service-area-list"), body, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_service_area(self):
        body = {
            "name": generator.word(),
            "price": random.uniform(0.1, 10000),
            "provider": ProviderFactory().pk,
            "area": get_random_coordinates(),
        }
        response = self.client.post(reverse("api_polygons:service-area-list"), body, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_service_area(self):
        service_area = self.service_areas[0]
        body = {"name": generator.word()}
        response = self.client.patch(
            reverse("api_polygons:service-area-detail", kwargs={"pk": service_area.pk}),
            body,
            format="json",
        )
        new_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(new_data.get("name"), service_area.name)

    def test_delete_service_area(self):
        service_area = self.service_areas[0]

        response = self.client.delete(
            reverse("api_polygons:service-area-detail", kwargs={"pk": service_area.pk}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
