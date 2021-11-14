from django.contrib import admin

from providers.models import Provider, Language, Currency


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    search_fields = ("name", "code",)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    search_fields = ("name", "code",)


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    search_fields = ("name", "email",)
    list_filter = ("language", "currency",)
    list_select_related = ("language", "currency")
