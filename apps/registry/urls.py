from django.urls import include, path
from rest_framework import routers
from apps.registry.views.person import PersonSearchView

from apps.registry.views.receipt import ReceiptCreateView, ReceiptDeleteView, ReceiptDetail, ReceiptSaveView, ReciptList
from apps.registry.views.service import ServiceCreateView, ServiceDeleteView, ServiceList, ServiceUpdateView

app_name = 'registry'
urlpatterns = [
    path('receipt/list', ReciptList.as_view(), name="receipt_list"),
    path('receipt/create', ReceiptCreateView.as_view(), name="receipt_create"),
    path('receipt/save', ReceiptSaveView.as_view(), name="receipt_save"),
    path('receipt/<uuid:pk>/detail', ReceiptDetail.as_view(), name="receipt_detail"),
    path('person/search', PersonSearchView.as_view(), name="person_search"),
    path('receipt/<uuid:pk>/delete', ReceiptDeleteView.as_view(), name="receipt_delete"),
    
    path('service/list', ServiceList.as_view(), name='service_list'),
    path('service/crear', ServiceCreateView.as_view(), name='service_create'),
    path('service/<uuid:pk>/update', ServiceUpdateView.as_view(), name='service_update'),
    path('service/<uuid:pk>/delete', ServiceDeleteView.as_view(), name='service_delete'),
]
