from rest_framework import serializers

from providers.models import Provider, Language, Currency


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("id", "name", "code")


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "name", "code")


class ProviderSerializer(serializers.ModelSerializer):
    language = serializers.PrimaryKeyRelatedField(required=True, queryset=Language.objects.all())
    currency = serializers.PrimaryKeyRelatedField(required=True, queryset=Currency.objects.all())

    class Meta:
        model = Provider
        fields = ("id", "name", "phone_number", "language", "currency")


class ProviderReadSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    currency = CurrencySerializer()

    class Meta:
        model = Provider
        fields = ("id", "name", "phone_number", "language", "currency")
