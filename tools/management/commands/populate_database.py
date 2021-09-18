""" Populate database command module """

import os
import json

from django.core.management.base import BaseCommand
from core.settings import BASE_DIR

from schemas.models.cities import City
from schemas.models.countries import Country



class Command(BaseCommand):
    help = "Populate the databse with multiple countries"
    mock_path = os.path.join(BASE_DIR, "tools", "mocks", "MOCK_DATA.json")

    def _load_json_file(self, filename:str) -> dict:
        """ read the filemane and return a dict """

        with open(filename) as rf:
            data = json.loads(rf.read())
        return data
    
    def _populate_cities(self, values:dict) -> None:
        """ populate city table """

        obj, created = City.objects.get_or_create(
            name=values.get("city"),
            state=values.get("state"),
            state_short=values.get("state_short"),
            postal_code=values.get("postal_code"),
        )

        if created:
            print(f"Created {obj.name}")


    def _populate_countries(self, values:dict) -> None:
        """ populate country table """

        try:
            _city = City.objects.get(name=values.get("city"))

            obj, created = Country.objects.get_or_create(
                name=values.get("country"),
                code=values.get("coutry_code"),
                timezone=values.get("timezone"),
                city=_city,
            )
            if created:
                print(f"Created {obj.name}")

        except (City.MultipleObjectsReturned, City.DoesNotExist) as exc:
            print(exc)
        
        



    def handle(self, *args, **options):
        
        data = self._load_json_file(self.mock_path)
        
        for element in data:
            self._populate_cities(element)
            self._populate_countries(element)


