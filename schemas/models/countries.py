""" Countries Schema Module """

from django.db import models
from schemas.models.mixins import TimeStampModel
from schemas.models.cities import City


class Country(TimeStampModel):
    name = models.CharField(verbose_name="País", max_length=128)
    code = models.CharField(verbose_name="Código", max_length=3, blank=True, null=True)
    timezone = models.CharField(verbose_name="Zona Horaria", max_length=128, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

    def __str__(self) -> str:
        return f"{self.name}"