from django.contrib import admin
from .models.person import Person
from .models.service import Service
from .models.receipt import Receipt
from .models.detail import Detail


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'cedule']
    list_filter = ('first_name', 'last_name')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['code', 'description', 'cost', 'is_public']
    list_filter = ('code',)


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ['number', 'client', 'total', 'date']
    list_filter = ('client__first_name', 'client__last_name', 'client__cedule')


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['receipt', 'service', 'cost']

