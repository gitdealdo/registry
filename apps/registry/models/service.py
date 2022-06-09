from uuid import uuid4
from django.db import models


class Service(models.Model):
    """
    - code
    - description
    - cost:decimal
    - is_public:boolean
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    code = models.CharField("Código", max_length=15)
    description = models.CharField("Descripción", max_length=35)
    cost = models.DecimalField("Costo", max_digits=7, decimal_places=2, default=0.00)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.description
