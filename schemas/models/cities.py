""" Cities Schema Module """

from django.db import models
from schemas.models.mixins import TimeStampModel

class City(TimeStampModel):
    name = models.CharField(verbose_name="Ciudad", max_length=128)
    state = models.CharField(verbose_name="Estado", max_length=64, blank=True, null=True)
    state_short = models.CharField(verbose_name="Código", max_length=3, blank=True, null=True)
    postal_code = models.CharField(verbose_name="Código Postal", max_length=32, blank=True, null=True)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self) -> str:
        return f"{self.name}"