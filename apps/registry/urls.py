from django.urls import include, path
from rest_framework import routers

from apps.registry.views.receipt import ReceiptCreateView, ReceiptDetail, ReciptList

app_name = 'registry'
urlpatterns = [
    path('receipt/list', ReciptList.as_view(), name="receipt_list"),
    path('receipt/create', ReceiptCreateView.as_view(), name="receipt_create"),
    path('receipt/<uuid:pk>/detail', ReceiptDetail.as_view(), name="receipt_detail"),
    # # path('usuarios/<int:pk>', UserDetailView.as_view(), name="user_detail"),
    # path('profile', UserProfileView.as_view(), name="user_profile"),
    # path('change-password/', change_password, name='change_password'),
]
