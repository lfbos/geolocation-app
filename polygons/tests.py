import random

import factory
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APITestCase

from providers.models import Provider

generator = Factory.create()


class ProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Provider

    name = generator.name()
    email = factory.Sequence(lambda _: f"{generator.name()}@mail.com")
    phone_number = factory.Faker("phone_number")
    language_id = random.choice((1, 2))
    currency_id = random.choice((1, 2, 3))


class ProviderTestCases(APITestCase):
    fixtures = ("languages", "currencies")

    def setUp(self) -> None:
        self.providers = ProviderFactory.create_batch(30)

    def test_list_languages(self):
        response = self.client.get(reverse("api_providers:languages"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_currencies(self):
        response = self.client.get(reverse("api_providers:currencies"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_providers(self):
        response = self.client.get(f"{reverse('api_providers:provider-list')}?page_size=10")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json().get("results")
        self.assertEqual(len(results), 10)

    def test_create_provider_with_missing_data(self):
        body = {"name": generator.name(), "email": f"{generator.name()}@mail.com"}
        response = self.client.post(reverse("api_providers:provider-list"), body, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_provider(self):
        body = {
            "name": generator.name(),
            "email": f"{generator.name()}@mail.com",
            "phone_number": "+56930787878",
            "language": 1,
            "currency": 1,
        }
        response = self.client.post(reverse("api_providers:provider-list"), body, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_provider(self):
        provider = self.providers[0]
        body = {"name": generator.name()}
        response = self.client.patch(
            reverse("api_providers:provider-detail", kwargs={"pk": provider.pk}),
            body,
            format="json",
        )
        new_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(new_data.get("name"), provider.name)

    def test_delete_provider(self):
        provider = self.providers[0]

        response = self.client.delete(
            reverse("api_providers:provider-detail", kwargs={"pk": provider.pk}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
