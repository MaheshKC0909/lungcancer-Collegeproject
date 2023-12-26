"""
URL configuration for lung_cancer_project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
    path('users/', include('apps.users.urls')),
    path('scans/', include('apps.ct_scans.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('predictions/', include('apps.predictions.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
