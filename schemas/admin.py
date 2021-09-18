from django.contrib import admin
from schemas.models.cities import City
from schemas.models.countries import Country



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "city",
        "timezone"
    )



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "state",
        "state_short",
        "postal_code",
    )


