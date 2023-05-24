from django.contrib import admin
from django.urls import path, include
from api import urls as api_urls


admin_pattern = [
    path("admin/", admin.site.urls),
]

urlpatterns = [
    path('', include((admin_pattern, 'admin'), namespace="backend")),
    path("api/", include(api_urls)),
]
