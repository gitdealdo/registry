from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views                                        #from django.views.generic import TemplateView              # Wire up our API using automatic URL routing.             # Additionally, we include login URLs for the browsable API
app_name = 'dauth'
urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

]

