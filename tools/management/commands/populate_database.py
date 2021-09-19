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

        try:
            _country = Country.objects.get(name=values.get("country"))

            obj, created = City.objects.get_or_create(
                name=values.get("city"),
                state=values.get("state"),
                country=_country,
                state_short=values.get("state_short"),
                postal_code=values.get("postal_code"),
            )

            if created:
                print(f"Created {obj.name}")
            else:
                pass

        except (Country.MultipleObjectsReturned, Country.DoesNotExist) as exc:
            print(exc)



    def handle(self, *args, **options):
        
        data = self._load_json_file(self.mock_path)
        
        for element in data:
            try:
                obj, created = Country.objects.get_or_create(
                    name=element.get("country"),
                    code=element.get("coutry_code"),
                    timezone=element.get("timezone"),
                )

                if created:
                    print(f"Created {obj.name}")

            except Exception as EXC:
                continue

        for element in data:
            self._populate_cities(element)



