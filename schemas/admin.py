from django.contrib import admin
from schemas.models.cities import City
from schemas.models.countries import Country



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "timezone"
    )

    search_fields = (
        "name",
    )



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "state",
        "country",
        "state_short",
        "postal_code",
    )

    search_fields = (
        "name",
        "country__name"
    )

