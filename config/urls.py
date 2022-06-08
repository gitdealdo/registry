from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.registry.views.dashboard import DashboardView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('admin/', admin.site.urls),
    # path('summernote/', include('django_summernote.urls')),
    path('dauth/', include('apps.dauth.urls'), name='dauth'),
    
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('account/', include('apps.account.urls'), name='account'),
    path('registry/', include('apps.registry.urls'), name='registry'),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
