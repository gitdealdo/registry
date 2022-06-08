from statistics import mode
from uuid import uuid4
from django.db import models

from .person import Person


class Receipt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    number = models.IntegerField()
    date = models.DateTimeField()
    client = models.ForeignKey(Person, related_name="receipts", on_delete=models.CASCADE)

    discount = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
  
    created_by = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comprobante"
        verbose_name_plural = "Comprobantes"

    def __str__(self):
        return "%s" % self.number
