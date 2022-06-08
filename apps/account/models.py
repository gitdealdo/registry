from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPES = (('ADMIN', 'Admin'), ('STAFF', 'Staff'))

class User(AbstractUser):
    """
    - identity_num
    - gender    
    - address
    - cellphone
    - birth_date
    - user_type: ADMIN, STAFF (for user admin)
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    identity_num = models.CharField("Número de identidad", max_length=20, blank=True, null=True, unique=True)
    address = models.CharField("Dirección", max_length=150, blank=True, null=True)
    cellphone = models.CharField("Celular", max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='ADMIN')
    updated_by = models.CharField(max_length=40, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    def full_name(self):
        return self.first_name + " " + self.last_name


class Company(models.Model):
    """
    - name
    - ruc
    - cellphone
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    ruc = models.CharField(max_length=11)
    cellphone = models.CharField(max_length=13)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name