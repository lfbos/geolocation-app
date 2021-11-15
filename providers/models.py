from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from utils.models import CommonInfo


class Language(models.Model):
    name = models.CharField(max_length=254, verbose_name="language name")
    code = models.CharField(max_length=64, verbose_name="language code")

    class Meta:
        verbose_name = "language"
        verbose_name_plural = "languages"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=254, verbose_name="currency name")
    code = models.CharField(max_length=64, verbose_name="currency code")

    class Meta:
        verbose_name = "currency"
        verbose_name_plural = "currencies"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Provider(CommonInfo):
    name = models.CharField(max_length=128, verbose_name="provider name")
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": "A provider with that email already exists.",
        },
        verbose_name="email address",
    )
    phone_number = PhoneNumberField(verbose_name="phone number")
    language = models.ForeignKey(
        "Language", related_name="providers", null=True, on_delete=models.SET_NULL
    )
    currency = models.ForeignKey(
        "Currency", related_name="providers", null=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "provider"
        verbose_name_plural = "providers"

    def __str__(self):
        return self.name
