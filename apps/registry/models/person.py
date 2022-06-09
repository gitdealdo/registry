from statistics import mode
from uuid import uuid4
from django.db import models


class Person(models.Model):
    """
    - first_name
    - last_name
    - cedule
    - email
    - cellphone
    - address
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField("Nombres", max_length=40)
    last_name = models.CharField("Apellidos", max_length=60)
    cedule = models.CharField("DNI", max_length=10, unique=True)
    email = models.EmailField("Correo", max_length=80, blank=True, null=True)
    cellphone = models.CharField("Celular", max_length=13, blank=True, null=True)
    address = models.CharField("Dirección", max_length=200)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.first_name
