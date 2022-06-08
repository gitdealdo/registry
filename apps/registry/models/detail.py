from uuid import uuid4
from django.db import models

from .receipt import Receipt
from .service import Service


class Detail(models.Model):
    """
    - registry
    - service
    - cost: from service cost
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    receipt = models.ForeignKey(Receipt, related_name='details', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = "Detail"
        verbose_name_plural = "Details"

    def __str__(self):
        return "%s" % self.receipt
