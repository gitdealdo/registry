from django.urls import include, path
from rest_framework import routers
from .views.user import UserProfileView, UserListView, change_password  # , UserDetailView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'account'
urlpatterns = [
    path('usuarios', UserListView.as_view(), name="user_list"),
    # path('usuarios/<int:pk>', UserDetailView.as_view(), name="user_detail"),
    path('profile', UserProfileView.as_view(), name="user_profile"),
    path('change-password/', change_password, name='change_password'),
]
